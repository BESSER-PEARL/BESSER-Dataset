from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class afpText_GCRLINERG:

    def __init__(self, XOSSF: str, YOFFS: str, afpText_GCRLINERG: "afpText_GCRLINE" = None):
        self.XOSSF = XOSSF
        self.YOFFS = YOFFS
        self.afpText_GCRLINERG = afpText_GCRLINERG
        
    @property
    def XOSSF(self) -> str:
        return self.__XOSSF

    @XOSSF.setter
    def XOSSF(self, XOSSF: str):
        self.__XOSSF = XOSSF

    @property
    def YOFFS(self) -> str:
        return self.__YOFFS

    @YOFFS.setter
    def YOFFS(self, YOFFS: str):
        self.__YOFFS = YOFFS

    @property
    def afpText_GCRLINERG(self):
        return self.__afpText_GCRLINERG

    @afpText_GCRLINERG.setter
    def afpText_GCRLINERG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_GCRLINERG__afpText_GCRLINERG", None)
        self.__afpText_GCRLINERG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_GCRLINE"):
                opp_val = getattr(old_value, "afpText_GCRLINE", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_GCRLINE"):
                opp_val = getattr(value, "afpText_GCRLINE", None)
                if opp_val is None:
                    setattr(value, "afpText_GCRLINE", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_GRLINERG:

    def __init__(self, XOSSF: str, YOFFS: str, afpText_GRLINERG: "afpText_GRLINE" = None):
        self.XOSSF = XOSSF
        self.YOFFS = YOFFS
        self.afpText_GRLINERG = afpText_GRLINERG
        
    @property
    def XOSSF(self) -> str:
        return self.__XOSSF

    @XOSSF.setter
    def XOSSF(self, XOSSF: str):
        self.__XOSSF = XOSSF

    @property
    def YOFFS(self) -> str:
        return self.__YOFFS

    @YOFFS.setter
    def YOFFS(self, YOFFS: str):
        self.__YOFFS = YOFFS

    @property
    def afpText_GRLINERG(self):
        return self.__afpText_GRLINERG

    @afpText_GRLINERG.setter
    def afpText_GRLINERG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_GRLINERG__afpText_GRLINERG", None)
        self.__afpText_GRLINERG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_GRLINE"):
                opp_val = getattr(old_value, "afpText_GRLINE", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_GRLINE"):
                opp_val = getattr(value, "afpText_GRLINE", None)
                if opp_val is None:
                    setattr(value, "afpText_GRLINE", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_GCMRKRG:

    def __init__(self, XPOS: str, YPOS: str, afpText_GCMRKRG: "afpText_GCMRK" = None):
        self.XPOS = XPOS
        self.YPOS = YPOS
        self.afpText_GCMRKRG = afpText_GCMRKRG
        
    @property
    def YPOS(self) -> str:
        return self.__YPOS

    @YPOS.setter
    def YPOS(self, YPOS: str):
        self.__YPOS = YPOS

    @property
    def XPOS(self) -> str:
        return self.__XPOS

    @XPOS.setter
    def XPOS(self, XPOS: str):
        self.__XPOS = XPOS

    @property
    def afpText_GCMRKRG(self):
        return self.__afpText_GCMRKRG

    @afpText_GCMRKRG.setter
    def afpText_GCMRKRG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_GCMRKRG__afpText_GCMRKRG", None)
        self.__afpText_GCMRKRG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_GCMRK"):
                opp_val = getattr(old_value, "afpText_GCMRK", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_GCMRK"):
                opp_val = getattr(value, "afpText_GCMRK", None)
                if opp_val is None:
                    setattr(value, "afpText_GCMRK", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_GMRKRG:

    def __init__(self, XPOS: str, YPOS: str, afpText_GMRKRG: "afpText_GMRK" = None):
        self.XPOS = XPOS
        self.YPOS = YPOS
        self.afpText_GMRKRG = afpText_GMRKRG
        
    @property
    def XPOS(self) -> str:
        return self.__XPOS

    @XPOS.setter
    def XPOS(self, XPOS: str):
        self.__XPOS = XPOS

    @property
    def YPOS(self) -> str:
        return self.__YPOS

    @YPOS.setter
    def YPOS(self, YPOS: str):
        self.__YPOS = YPOS

    @property
    def afpText_GMRKRG(self):
        return self.__afpText_GMRKRG

    @afpText_GMRKRG.setter
    def afpText_GMRKRG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_GMRKRG__afpText_GMRKRG", None)
        self.__afpText_GMRKRG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_GMRK"):
                opp_val = getattr(old_value, "afpText_GMRK", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_GMRK"):
                opp_val = getattr(value, "afpText_GMRK", None)
                if opp_val is None:
                    setattr(value, "afpText_GMRK", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class triplet:

    pass
class afpText_GSMT(triplet):

    def __init__(self, MCPT: str):
        self.MCPT = MCPT
        
    @property
    def MCPT(self) -> str:
        return self.__MCPT

    @MCPT.setter
    def MCPT(self, MCPT: str):
        self.__MCPT = MCPT

class afpText_DeviceAppearance(triplet):

    def __init__(self, DevApp: str, Reserved: str):
        self.DevApp = DevApp
        self.Reserved = Reserved
        
    @property
    def Reserved(self) -> str:
        return self.__Reserved

    @Reserved.setter
    def Reserved(self, Reserved: str):
        self.__Reserved = Reserved

    @property
    def DevApp(self) -> str:
        return self.__DevApp

    @DevApp.setter
    def DevApp(self, DevApp: str):
        self.__DevApp = DevApp

class afpText_FNNRG2(triplet):

    def __init__(self, TSIDLen: str, TSID: str):
        self.TSIDLen = TSIDLen
        self.TSID = TSID
        
    @property
    def TSID(self) -> str:
        return self.__TSID

    @TSID.setter
    def TSID(self, TSID: str):
        self.__TSID = TSID

    @property
    def TSIDLen(self) -> str:
        return self.__TSIDLen

    @TSIDLen.setter
    def TSIDLen(self, TSIDLen: str):
        self.__TSIDLen = TSIDLen

class afpText_ColorSpecification(triplet):

    def __init__(self, ColSpce: str, ColSize1: str, ColSize2: str, ColSize3: str, ColSize4: str, Color: str):
        self.ColSpce = ColSpce
        self.ColSize1 = ColSize1
        self.ColSize2 = ColSize2
        self.ColSize3 = ColSize3
        self.ColSize4 = ColSize4
        self.Color = Color
        
    @property
    def ColSize1(self) -> str:
        return self.__ColSize1

    @ColSize1.setter
    def ColSize1(self, ColSize1: str):
        self.__ColSize1 = ColSize1

    @property
    def Color(self) -> str:
        return self.__Color

    @Color.setter
    def Color(self, Color: str):
        self.__Color = Color

    @property
    def ColSpce(self) -> str:
        return self.__ColSpce

    @ColSpce.setter
    def ColSpce(self, ColSpce: str):
        self.__ColSpce = ColSpce

    @property
    def ColSize3(self) -> str:
        return self.__ColSize3

    @ColSize3.setter
    def ColSize3(self, ColSize3: str):
        self.__ColSize3 = ColSize3

    @property
    def ColSize4(self) -> str:
        return self.__ColSize4

    @ColSize4.setter
    def ColSize4(self, ColSize4: str):
        self.__ColSize4 = ColSize4

    @property
    def ColSize2(self) -> str:
        return self.__ColSize2

    @ColSize2.setter
    def ColSize2(self, ColSize2: str):
        self.__ColSize2 = ColSize2

class afpText_BeginTile(triplet):

    pass
class afpText_STC(triplet):

    def __init__(self, FRGCOLOR: str, PRECSION: str):
        self.FRGCOLOR = FRGCOLOR
        self.PRECSION = PRECSION
        
    @property
    def FRGCOLOR(self) -> str:
        return self.__FRGCOLOR

    @FRGCOLOR.setter
    def FRGCOLOR(self, FRGCOLOR: str):
        self.__FRGCOLOR = FRGCOLOR

    @property
    def PRECSION(self) -> str:
        return self.__PRECSION

    @PRECSION.setter
    def PRECSION(self, PRECSION: str):
        self.__PRECSION = PRECSION

class afpText_FullyQualifiedName(triplet):

    def __init__(self, FQNType: str, FQNFormat: str, FQName: str):
        self.FQNType = FQNType
        self.FQNFormat = FQNFormat
        self.FQName = FQName
        
    @property
    def FQNType(self) -> str:
        return self.__FQNType

    @FQNType.setter
    def FQNType(self, FQNType: str):
        self.__FQNType = FQNType

    @property
    def FQNFormat(self) -> str:
        return self.__FQNFormat

    @FQNFormat.setter
    def FQNFormat(self, FQNFormat: str):
        self.__FQNFormat = FQNFormat

    @property
    def FQName(self) -> str:
        return self.__FQName

    @FQName.setter
    def FQName(self, FQName: str):
        self.__FQName = FQName

class afpText_MediumMapPageNumber(triplet):

    def __init__(self, PageNum: str):
        self.PageNum = PageNum
        
    @property
    def PageNum(self) -> str:
        return self.__PageNum

    @PageNum.setter
    def PageNum(self, PageNum: str):
        self.__PageNum = PageNum

class afpText_EndTile(triplet):

    pass
class afpText_GSCH(triplet):

    def __init__(self, HX: str, HY: str):
        self.HX = HX
        self.HY = HY
        
    @property
    def HY(self) -> str:
        return self.__HY

    @HY.setter
    def HY(self, HY: str):
        self.__HY = HY

    @property
    def HX(self) -> str:
        return self.__HX

    @HX.setter
    def HX(self, HX: str):
        self.__HX = HX

class afpText_GSECOL(triplet):

    def __init__(self, COLOR: str):
        self.COLOR = COLOR
        
    @property
    def COLOR(self) -> str:
        return self.__COLOR

    @COLOR.setter
    def COLOR(self, COLOR: str):
        self.__COLOR = COLOR

class afpText_GSCC(triplet):

    def __init__(self, CELLWI: str, CELLHI: str, CELLWFR: str, CELLHFR: str):
        self.CELLWI = CELLWI
        self.CELLHI = CELLHI
        self.CELLWFR = CELLWFR
        self.CELLHFR = CELLHFR
        
    @property
    def CELLWI(self) -> str:
        return self.__CELLWI

    @CELLWI.setter
    def CELLWI(self, CELLWI: str):
        self.__CELLWI = CELLWI

    @property
    def CELLHI(self) -> str:
        return self.__CELLHI

    @CELLHI.setter
    def CELLHI(self, CELLHI: str):
        self.__CELLHI = CELLHI

    @property
    def CELLHFR(self) -> str:
        return self.__CELLHFR

    @CELLHFR.setter
    def CELLHFR(self, CELLHFR: str):
        self.__CELLHFR = CELLHFR

    @property
    def CELLWFR(self) -> str:
        return self.__CELLWFR

    @CELLWFR.setter
    def CELLWFR(self, CELLWFR: str):
        self.__CELLWFR = CELLWFR

class afpText_GCBOX(triplet):

    def __init__(self, RES: str, XPOS1: str, YPOS1: str, HAXIS: str, VAXIS: str):
        self.RES = RES
        self.XPOS1 = XPOS1
        self.YPOS1 = YPOS1
        self.HAXIS = HAXIS
        self.VAXIS = VAXIS
        
    @property
    def HAXIS(self) -> str:
        return self.__HAXIS

    @HAXIS.setter
    def HAXIS(self, HAXIS: str):
        self.__HAXIS = HAXIS

    @property
    def XPOS1(self) -> str:
        return self.__XPOS1

    @XPOS1.setter
    def XPOS1(self, XPOS1: str):
        self.__XPOS1 = XPOS1

    @property
    def YPOS1(self) -> str:
        return self.__YPOS1

    @YPOS1.setter
    def YPOS1(self, YPOS1: str):
        self.__YPOS1 = YPOS1

    @property
    def VAXIS(self) -> str:
        return self.__VAXIS

    @VAXIS.setter
    def VAXIS(self, VAXIS: str):
        self.__VAXIS = VAXIS

    @property
    def RES(self) -> str:
        return self.__RES

    @RES.setter
    def RES(self, RES: str):
        self.__RES = RES

class afpText_AttributeQualifier(triplet):

    def __init__(self, SeqNum: str, LevNum: str):
        self.SeqNum = SeqNum
        self.LevNum = LevNum
        
    @property
    def SeqNum(self) -> str:
        return self.__SeqNum

    @SeqNum.setter
    def SeqNum(self, SeqNum: str):
        self.__SeqNum = SeqNum

    @property
    def LevNum(self) -> str:
        return self.__LevNum

    @LevNum.setter
    def LevNum(self, LevNum: str):
        self.__LevNum = LevNum

class afpText_MetricAdjustment(triplet):

    def __init__(self, UnitBase: str, XUPUB: str, YUPUB: str, HUniformIncrement: str, VUniformIncrement: str, HBaselineIncrement: str, VBaselineIncrement: str):
        self.UnitBase = UnitBase
        self.XUPUB = XUPUB
        self.YUPUB = YUPUB
        self.HUniformIncrement = HUniformIncrement
        self.VUniformIncrement = VUniformIncrement
        self.HBaselineIncrement = HBaselineIncrement
        self.VBaselineIncrement = VBaselineIncrement
        
    @property
    def HBaselineIncrement(self) -> str:
        return self.__HBaselineIncrement

    @HBaselineIncrement.setter
    def HBaselineIncrement(self, HBaselineIncrement: str):
        self.__HBaselineIncrement = HBaselineIncrement

    @property
    def HUniformIncrement(self) -> str:
        return self.__HUniformIncrement

    @HUniformIncrement.setter
    def HUniformIncrement(self, HUniformIncrement: str):
        self.__HUniformIncrement = HUniformIncrement

    @property
    def XUPUB(self) -> str:
        return self.__XUPUB

    @XUPUB.setter
    def XUPUB(self, XUPUB: str):
        self.__XUPUB = XUPUB

    @property
    def VUniformIncrement(self) -> str:
        return self.__VUniformIncrement

    @VUniformIncrement.setter
    def VUniformIncrement(self, VUniformIncrement: str):
        self.__VUniformIncrement = VUniformIncrement

    @property
    def VBaselineIncrement(self) -> str:
        return self.__VBaselineIncrement

    @VBaselineIncrement.setter
    def VBaselineIncrement(self, VBaselineIncrement: str):
        self.__VBaselineIncrement = VBaselineIncrement

    @property
    def UnitBase(self) -> str:
        return self.__UnitBase

    @UnitBase.setter
    def UnitBase(self, UnitBase: str):
        self.__UnitBase = UnitBase

    @property
    def YUPUB(self) -> str:
        return self.__YUPUB

    @YUPUB.setter
    def YUPUB(self, YUPUB: str):
        self.__YUPUB = YUPUB

class afpText_RPS(triplet):

    def __init__(self, RLENGTH: str, RPTDATA: str):
        self.RLENGTH = RLENGTH
        self.RPTDATA = RPTDATA
        
    @property
    def RLENGTH(self) -> str:
        return self.__RLENGTH

    @RLENGTH.setter
    def RLENGTH(self, RLENGTH: str):
        self.__RLENGTH = RLENGTH

    @property
    def RPTDATA(self) -> str:
        return self.__RPTDATA

    @RPTDATA.setter
    def RPTDATA(self, RPTDATA: str):
        self.__RPTDATA = RPTDATA

class afpText_RMI(triplet):

    def __init__(self, INCRMENT: str):
        self.INCRMENT = INCRMENT
        
    @property
    def INCRMENT(self) -> str:
        return self.__INCRMENT

    @INCRMENT.setter
    def INCRMENT(self, INCRMENT: str):
        self.__INCRMENT = INCRMENT

class afpText_ExtensionFont(triplet):

    def __init__(self, GCSGID: str):
        self.GCSGID = GCSGID
        
    @property
    def GCSGID(self) -> str:
        return self.__GCSGID

    @GCSGID.setter
    def GCSGID(self, GCSGID: str):
        self.__GCSGID = GCSGID

class afpText_Comment(triplet):

    def __init__(self, Comment: str):
        self.Comment = Comment
        
    @property
    def Comment(self) -> str:
        return self.__Comment

    @Comment.setter
    def Comment(self, Comment: str):
        self.__Comment = Comment

class afpText_EndSegment(triplet):

    pass
class afpText_ObjectClassification(triplet):

    def __init__(self, ObjClass: str, StrucFlgs: str, RegObjId: str, ObjTpName: str, ObjLev: str, CompName: str):
        self.ObjClass = ObjClass
        self.StrucFlgs = StrucFlgs
        self.RegObjId = RegObjId
        self.ObjTpName = ObjTpName
        self.ObjLev = ObjLev
        self.CompName = CompName
        
    @property
    def ObjTpName(self) -> str:
        return self.__ObjTpName

    @ObjTpName.setter
    def ObjTpName(self, ObjTpName: str):
        self.__ObjTpName = ObjTpName

    @property
    def StrucFlgs(self) -> str:
        return self.__StrucFlgs

    @StrucFlgs.setter
    def StrucFlgs(self, StrucFlgs: str):
        self.__StrucFlgs = StrucFlgs

    @property
    def CompName(self) -> str:
        return self.__CompName

    @CompName.setter
    def CompName(self, CompName: str):
        self.__CompName = CompName

    @property
    def RegObjId(self) -> str:
        return self.__RegObjId

    @RegObjId.setter
    def RegObjId(self, RegObjId: str):
        self.__RegObjId = RegObjId

    @property
    def ObjLev(self) -> str:
        return self.__ObjLev

    @ObjLev.setter
    def ObjLev(self, ObjLev: str):
        self.__ObjLev = ObjLev

    @property
    def ObjClass(self) -> str:
        return self.__ObjClass

    @ObjClass.setter
    def ObjClass(self, ObjClass: str):
        self.__ObjClass = ObjClass

class afpText_DescriptorPosition(triplet):

    def __init__(self, DesPosID: str):
        self.DesPosID = DesPosID
        
    @property
    def DesPosID(self) -> str:
        return self.__DesPosID

    @DesPosID.setter
    def DesPosID(self, DesPosID: str):
        self.__DesPosID = DesPosID

class afpText_EndSegmentCommand(triplet):

    pass
class afpText_CRCResourceManagement(triplet):

    def __init__(self, FmtQual: str, RMValue: str, ResClassFlg: str):
        self.FmtQual = FmtQual
        self.RMValue = RMValue
        self.ResClassFlg = ResClassFlg
        
    @property
    def RMValue(self) -> str:
        return self.__RMValue

    @RMValue.setter
    def RMValue(self, RMValue: str):
        self.__RMValue = RMValue

    @property
    def FmtQual(self) -> str:
        return self.__FmtQual

    @FmtQual.setter
    def FmtQual(self, FmtQual: str):
        self.__FmtQual = FmtQual

    @property
    def ResClassFlg(self) -> str:
        return self.__ResClassFlg

    @ResClassFlg.setter
    def ResClassFlg(self, ResClassFlg: str):
        self.__ResClassFlg = ResClassFlg

class afpText_BSU(triplet):

    def __init__(self, LID: str):
        self.LID = LID
        
    @property
    def LID(self) -> str:
        return self.__LID

    @LID.setter
    def LID(self, LID: str):
        self.__LID = LID

class afpText_IOCAFunctionSetIdentification(triplet):

    def __init__(self, CATEGORY: str, FCNSET: str):
        self.CATEGORY = CATEGORY
        self.FCNSET = FCNSET
        
    @property
    def CATEGORY(self) -> str:
        return self.__CATEGORY

    @CATEGORY.setter
    def CATEGORY(self, CATEGORY: str):
        self.__CATEGORY = CATEGORY

    @property
    def FCNSET(self) -> str:
        return self.__FCNSET

    @FCNSET.setter
    def FCNSET(self, FCNSET: str):
        self.__FCNSET = FCNSET

class afpText_ObjectAreaSize(triplet):

    def __init__(self, SizeType: str, XoaSize: str, YoaSize: str):
        self.SizeType = SizeType
        self.XoaSize = XoaSize
        self.YoaSize = YoaSize
        
    @property
    def YoaSize(self) -> str:
        return self.__YoaSize

    @YoaSize.setter
    def YoaSize(self, YoaSize: str):
        self.__YoaSize = YoaSize

    @property
    def SizeType(self) -> str:
        return self.__SizeType

    @SizeType.setter
    def SizeType(self, SizeType: str):
        self.__SizeType = SizeType

    @property
    def XoaSize(self) -> str:
        return self.__XoaSize

    @XoaSize.setter
    def XoaSize(self, XoaSize: str):
        self.__XoaSize = XoaSize

class afpText_GCBEZ(triplet):

    pass
class afpText_TBM(triplet):

    def __init__(self, DIRCTION: str, PRECSION: str, INCRMENT: str):
        self.DIRCTION = DIRCTION
        self.PRECSION = PRECSION
        self.INCRMENT = INCRMENT
        
    @property
    def PRECSION(self) -> str:
        return self.__PRECSION

    @PRECSION.setter
    def PRECSION(self, PRECSION: str):
        self.__PRECSION = PRECSION

    @property
    def INCRMENT(self) -> str:
        return self.__INCRMENT

    @INCRMENT.setter
    def INCRMENT(self, INCRMENT: str):
        self.__INCRMENT = INCRMENT

    @property
    def DIRCTION(self) -> str:
        return self.__DIRCTION

    @DIRCTION.setter
    def DIRCTION(self, DIRCTION: str):
        self.__DIRCTION = DIRCTION

class afpText_RenderingIntent(triplet):

    def __init__(self, Reserved: str, IOCARI: str, OCRI: str, PTOCRI: str, GOCARI: str, Reserved2: str):
        self.Reserved = Reserved
        self.IOCARI = IOCARI
        self.OCRI = OCRI
        self.PTOCRI = PTOCRI
        self.GOCARI = GOCARI
        self.Reserved2 = Reserved2
        
    @property
    def Reserved2(self) -> str:
        return self.__Reserved2

    @Reserved2.setter
    def Reserved2(self, Reserved2: str):
        self.__Reserved2 = Reserved2

    @property
    def Reserved(self) -> str:
        return self.__Reserved

    @Reserved.setter
    def Reserved(self, Reserved: str):
        self.__Reserved = Reserved

    @property
    def GOCARI(self) -> str:
        return self.__GOCARI

    @GOCARI.setter
    def GOCARI(self, GOCARI: str):
        self.__GOCARI = GOCARI

    @property
    def PTOCRI(self) -> str:
        return self.__PTOCRI

    @PTOCRI.setter
    def PTOCRI(self, PTOCRI: str):
        self.__PTOCRI = PTOCRI

    @property
    def IOCARI(self) -> str:
        return self.__IOCARI

    @IOCARI.setter
    def IOCARI(self, IOCARI: str):
        self.__IOCARI = IOCARI

    @property
    def OCRI(self) -> str:
        return self.__OCRI

    @OCRI.setter
    def OCRI(self, OCRI: str):
        self.__OCRI = OCRI

class afpText_GBAR(triplet):

    def __init__(self, FLAGS: str):
        self.FLAGS = FLAGS
        
    @property
    def FLAGS(self) -> str:
        return self.__FLAGS

    @FLAGS.setter
    def FLAGS(self, FLAGS: str):
        self.__FLAGS = FLAGS

class afpText_GSMC(triplet):

    def __init__(self, CELLWI: str, CELLHI: str):
        self.CELLWI = CELLWI
        self.CELLHI = CELLHI
        
    @property
    def CELLHI(self) -> str:
        return self.__CELLHI

    @CELLHI.setter
    def CELLHI(self, CELLHI: str):
        self.__CELLHI = CELLHI

    @property
    def CELLWI(self) -> str:
        return self.__CELLWI

    @CELLWI.setter
    def CELLWI(self, CELLWI: str):
        self.__CELLWI = CELLWI

class afpText_IDESize(triplet):

    def __init__(self, IDESZ: str):
        self.IDESZ = IDESZ
        
    @property
    def IDESZ(self) -> str:
        return self.__IDESZ

    @IDESZ.setter
    def IDESZ(self, IDESZ: str):
        self.__IDESZ = IDESZ

class afpText_GEPROL(triplet):

    def __init__(self, RES: str):
        self.RES = RES
        
    @property
    def RES(self) -> str:
        return self.__RES

    @RES.setter
    def RES(self, RES: str):
        self.__RES = RES

class afpText_GCMRK(triplet):

    pass
class afpText_RMB(triplet):

    def __init__(self, INCRMENT: str):
        self.INCRMENT = INCRMENT
        
    @property
    def INCRMENT(self) -> str:
        return self.__INCRMENT

    @INCRMENT.setter
    def INCRMENT(self, INCRMENT: str):
        self.__INCRMENT = INCRMENT

class afpText_GSCOL(triplet):

    def __init__(self, COL: str):
        self.COL = COL
        
    @property
    def COL(self) -> str:
        return self.__COL

    @COL.setter
    def COL(self, COL: str):
        self.__COL = COL

class afpText_SIM(triplet):

    def __init__(self, DSPLCMNT: str):
        self.DSPLCMNT = DSPLCMNT
        
    @property
    def DSPLCMNT(self) -> str:
        return self.__DSPLCMNT

    @DSPLCMNT.setter
    def DSPLCMNT(self, DSPLCMNT: str):
        self.__DSPLCMNT = DSPLCMNT

class afpText_TilePosition(triplet):

    def __init__(self, XOFFSET: str, YOFFSET: str):
        self.XOFFSET = XOFFSET
        self.YOFFSET = YOFFSET
        
    @property
    def XOFFSET(self) -> str:
        return self.__XOFFSET

    @XOFFSET.setter
    def XOFFSET(self, XOFFSET: str):
        self.__XOFFSET = XOFFSET

    @property
    def YOFFSET(self) -> str:
        return self.__YOFFSET

    @YOFFSET.setter
    def YOFFSET(self, YOFFSET: str):
        self.__YOFFSET = YOFFSET

class afpText_GSPCOL(triplet):

    def __init__(self, COLVALUE: str, RES1: str, COLSPCE: str, RES2: str, COLSIZE1: str, COLSIZE2: str, COLSIZE3: str, COLSIZE4: str):
        self.COLVALUE = COLVALUE
        self.RES1 = RES1
        self.COLSPCE = COLSPCE
        self.RES2 = RES2
        self.COLSIZE1 = COLSIZE1
        self.COLSIZE2 = COLSIZE2
        self.COLSIZE3 = COLSIZE3
        self.COLSIZE4 = COLSIZE4
        
    @property
    def RES1(self) -> str:
        return self.__RES1

    @RES1.setter
    def RES1(self, RES1: str):
        self.__RES1 = RES1

    @property
    def COLSIZE2(self) -> str:
        return self.__COLSIZE2

    @COLSIZE2.setter
    def COLSIZE2(self, COLSIZE2: str):
        self.__COLSIZE2 = COLSIZE2

    @property
    def COLSPCE(self) -> str:
        return self.__COLSPCE

    @COLSPCE.setter
    def COLSPCE(self, COLSPCE: str):
        self.__COLSPCE = COLSPCE

    @property
    def COLSIZE1(self) -> str:
        return self.__COLSIZE1

    @COLSIZE1.setter
    def COLSIZE1(self, COLSIZE1: str):
        self.__COLSIZE1 = COLSIZE1

    @property
    def COLVALUE(self) -> str:
        return self.__COLVALUE

    @COLVALUE.setter
    def COLVALUE(self, COLVALUE: str):
        self.__COLVALUE = COLVALUE

    @property
    def COLSIZE3(self) -> str:
        return self.__COLSIZE3

    @COLSIZE3.setter
    def COLSIZE3(self, COLSIZE3: str):
        self.__COLSIZE3 = COLSIZE3

    @property
    def RES2(self) -> str:
        return self.__RES2

    @RES2.setter
    def RES2(self, RES2: str):
        self.__RES2 = RES2

    @property
    def COLSIZE4(self) -> str:
        return self.__COLSIZE4

    @COLSIZE4.setter
    def COLSIZE4(self, COLSIZE4: str):
        self.__COLSIZE4 = COLSIZE4

class afpText_ExtendedResourceLocalIdentifier(triplet):

    def __init__(self, ResType: str, ResLID: str):
        self.ResType = ResType
        self.ResLID = ResLID
        
    @property
    def ResType(self) -> str:
        return self.__ResType

    @ResType.setter
    def ResType(self, ResType: str):
        self.__ResType = ResType

    @property
    def ResLID(self) -> str:
        return self.__ResLID

    @ResLID.setter
    def ResLID(self, ResLID: str):
        self.__ResLID = ResLID

class afpText_GSMS(triplet):

    def __init__(self, LCID: str):
        self.LCID = LCID
        
    @property
    def LCID(self) -> str:
        return self.__LCID

    @LCID.setter
    def LCID(self, LCID: str):
        self.__LCID = LCID

class afpText_PageOverlayConditionalProcessing(triplet):

    def __init__(self, PgOvType: str, Level: str):
        self.PgOvType = PgOvType
        self.Level = Level
        
    @property
    def Level(self) -> str:
        return self.__Level

    @Level.setter
    def Level(self, Level: str):
        self.__Level = Level

    @property
    def PgOvType(self) -> str:
        return self.__PgOvType

    @PgOvType.setter
    def PgOvType(self, PgOvType: str):
        self.__PgOvType = PgOvType

class afpText_ObjectStructuredFieldExtent(triplet):

    def __init__(self, SFExt: str, SFExtHi: str):
        self.SFExt = SFExt
        self.SFExtHi = SFExtHi
        
    @property
    def SFExt(self) -> str:
        return self.__SFExt

    @SFExt.setter
    def SFExt(self, SFExt: str):
        self.__SFExt = SFExt

    @property
    def SFExtHi(self) -> str:
        return self.__SFExtHi

    @SFExtHi.setter
    def SFExtHi(self, SFExtHi: str):
        self.__SFExtHi = SFExtHi

class afpText_GEAR(triplet):

    def __init__(self, DATA: str):
        self.DATA = DATA
        
    @property
    def DATA(self) -> str:
        return self.__DATA

    @DATA.setter
    def DATA(self, DATA: str):
        self.__DATA = DATA

class afpText_LineDataObjectPositionMigration(triplet):

    def __init__(self, TempOrient: str):
        self.TempOrient = TempOrient
        
    @property
    def TempOrient(self) -> str:
        return self.__TempOrient

    @TempOrient.setter
    def TempOrient(self, TempOrient: str):
        self.__TempOrient = TempOrient

class afpText_PresentationSpaceMixingRules(triplet):

    pass
class afpText_MediaEjectControl(triplet):

    def __init__(self, Reserved: str, EjCtrl: str):
        self.Reserved = Reserved
        self.EjCtrl = EjCtrl
        
    @property
    def EjCtrl(self) -> str:
        return self.__EjCtrl

    @EjCtrl.setter
    def EjCtrl(self, EjCtrl: str):
        self.__EjCtrl = EjCtrl

    @property
    def Reserved(self) -> str:
        return self.__Reserved

    @Reserved.setter
    def Reserved(self, Reserved: str):
        self.__Reserved = Reserved

class afpText_GSGCH(triplet):

    pass
class afpText_GFLT(triplet):

    pass
class afpText_EndTransparencyMask(triplet):

    pass
class afpText_BandImage(triplet):

    def __init__(self, BCOUNT: str, afpText_BandImage: set["afpText_BandImageRG"] = None):
        self.BCOUNT = BCOUNT
        self.afpText_BandImage = afpText_BandImage if afpText_BandImage is not None else set()
        
    @property
    def BCOUNT(self) -> str:
        return self.__BCOUNT

    @BCOUNT.setter
    def BCOUNT(self, BCOUNT: str):
        self.__BCOUNT = BCOUNT

    @property
    def afpText_BandImage(self):
        return self.__afpText_BandImage

    @afpText_BandImage.setter
    def afpText_BandImage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_BandImage__afpText_BandImage", None)
        self.__afpText_BandImage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_BandImageRG"):
                    opp_val = getattr(item, "afpText_BandImageRG", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_BandImageRG", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_BandImageRG"):
                    opp_val = getattr(item, "afpText_BandImageRG", None)
                    
                    setattr(item, "afpText_BandImageRG", self)
                    

class afpText_MODCAInterchangeSet(triplet):

    def __init__(self, IStype: str, ISid: str):
        self.IStype = IStype
        self.ISid = ISid
        
    @property
    def IStype(self) -> str:
        return self.__IStype

    @IStype.setter
    def IStype(self, IStype: str):
        self.__IStype = IStype

    @property
    def ISid(self) -> str:
        return self.__ISid

    @ISid.setter
    def ISid(self, ISid: str):
        self.__ISid = ISid

class afpText_ImageData(triplet):

    def __init__(self, DATA: str):
        self.DATA = DATA
        
    @property
    def DATA(self) -> str:
        return self.__DATA

    @DATA.setter
    def DATA(self, DATA: str):
        self.__DATA = DATA

class afpText_MappingOption(triplet):

    def __init__(self, MapValue: str):
        self.MapValue = MapValue
        
    @property
    def MapValue(self) -> str:
        return self.__MapValue

    @MapValue.setter
    def MapValue(self, MapValue: str):
        self.__MapValue = MapValue

class afpText_SCFL(triplet):

    def __init__(self, LID: str):
        self.LID = LID
        
    @property
    def LID(self) -> str:
        return self.__LID

    @LID.setter
    def LID(self, LID: str):
        self.__LID = LID

class afpText_GSLE(triplet):

    def __init__(self, LINEEND: str):
        self.LINEEND = LINEEND
        
    @property
    def LINEEND(self) -> str:
        return self.__LINEEND

    @LINEEND.setter
    def LINEEND(self, LINEEND: str):
        self.__LINEEND = LINEEND

class afpText_UniversalDateAndTimeStamp(triplet):

    def __init__(self, Reserved: str, YearAD: str, Month: str, Day: str, Hour: str, Minute: str, Second: str, TimeZone: str, UTCDiffH: str, UTCDiffM: str):
        self.Reserved = Reserved
        self.YearAD = YearAD
        self.Month = Month
        self.Day = Day
        self.Hour = Hour
        self.Minute = Minute
        self.Second = Second
        self.TimeZone = TimeZone
        self.UTCDiffH = UTCDiffH
        self.UTCDiffM = UTCDiffM
        
    @property
    def TimeZone(self) -> str:
        return self.__TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone: str):
        self.__TimeZone = TimeZone

    @property
    def Day(self) -> str:
        return self.__Day

    @Day.setter
    def Day(self, Day: str):
        self.__Day = Day

    @property
    def Second(self) -> str:
        return self.__Second

    @Second.setter
    def Second(self, Second: str):
        self.__Second = Second

    @property
    def UTCDiffM(self) -> str:
        return self.__UTCDiffM

    @UTCDiffM.setter
    def UTCDiffM(self, UTCDiffM: str):
        self.__UTCDiffM = UTCDiffM

    @property
    def UTCDiffH(self) -> str:
        return self.__UTCDiffH

    @UTCDiffH.setter
    def UTCDiffH(self, UTCDiffH: str):
        self.__UTCDiffH = UTCDiffH

    @property
    def Month(self) -> str:
        return self.__Month

    @Month.setter
    def Month(self, Month: str):
        self.__Month = Month

    @property
    def YearAD(self) -> str:
        return self.__YearAD

    @YearAD.setter
    def YearAD(self, YearAD: str):
        self.__YearAD = YearAD

    @property
    def Hour(self) -> str:
        return self.__Hour

    @Hour.setter
    def Hour(self, Hour: str):
        self.__Hour = Hour

    @property
    def Minute(self) -> str:
        return self.__Minute

    @Minute.setter
    def Minute(self, Minute: str):
        self.__Minute = Minute

    @property
    def Reserved(self) -> str:
        return self.__Reserved

    @Reserved.setter
    def Reserved(self, Reserved: str):
        self.__Reserved = Reserved

class afpText_EndImage(triplet):

    pass
class afpText_GCRLINE(triplet):

    pass
class afpText_BeginTransparencyMask(triplet):

    pass
class afpText_TileSetColor(triplet):

    def __init__(self, SIZE1: str, SIZE2: str, SIZE3: str, SIZE4: str, CVAL1: str, CVAL2: str, CVAL3: str, CVAL4: str, CSPACE: str, RESERVED: str):
        self.SIZE1 = SIZE1
        self.SIZE2 = SIZE2
        self.SIZE3 = SIZE3
        self.SIZE4 = SIZE4
        self.CVAL1 = CVAL1
        self.CVAL2 = CVAL2
        self.CVAL3 = CVAL3
        self.CVAL4 = CVAL4
        self.CSPACE = CSPACE
        self.RESERVED = RESERVED
        
    @property
    def CVAL3(self) -> str:
        return self.__CVAL3

    @CVAL3.setter
    def CVAL3(self, CVAL3: str):
        self.__CVAL3 = CVAL3

    @property
    def RESERVED(self) -> str:
        return self.__RESERVED

    @RESERVED.setter
    def RESERVED(self, RESERVED: str):
        self.__RESERVED = RESERVED

    @property
    def CVAL4(self) -> str:
        return self.__CVAL4

    @CVAL4.setter
    def CVAL4(self, CVAL4: str):
        self.__CVAL4 = CVAL4

    @property
    def CVAL2(self) -> str:
        return self.__CVAL2

    @CVAL2.setter
    def CVAL2(self, CVAL2: str):
        self.__CVAL2 = CVAL2

    @property
    def SIZE3(self) -> str:
        return self.__SIZE3

    @SIZE3.setter
    def SIZE3(self, SIZE3: str):
        self.__SIZE3 = SIZE3

    @property
    def SIZE2(self) -> str:
        return self.__SIZE2

    @SIZE2.setter
    def SIZE2(self, SIZE2: str):
        self.__SIZE2 = SIZE2

    @property
    def SIZE1(self) -> str:
        return self.__SIZE1

    @SIZE1.setter
    def SIZE1(self, SIZE1: str):
        self.__SIZE1 = SIZE1

    @property
    def CSPACE(self) -> str:
        return self.__CSPACE

    @CSPACE.setter
    def CSPACE(self, CSPACE: str):
        self.__CSPACE = CSPACE

    @property
    def SIZE4(self) -> str:
        return self.__SIZE4

    @SIZE4.setter
    def SIZE4(self, SIZE4: str):
        self.__SIZE4 = SIZE4

    @property
    def CVAL1(self) -> str:
        return self.__CVAL1

    @CVAL1.setter
    def CVAL1(self, CVAL1: str):
        self.__CVAL1 = CVAL1

class afpText_AMI(triplet):

    def __init__(self, DSPLCMNT: str):
        self.DSPLCMNT = DSPLCMNT
        
    @property
    def DSPLCMNT(self) -> str:
        return self.__DSPLCMNT

    @DSPLCMNT.setter
    def DSPLCMNT(self, DSPLCMNT: str):
        self.__DSPLCMNT = DSPLCMNT

class afpText_TextFidelity(triplet):

    def __init__(self, StpTxtEx: str, RepTxtEx: str):
        self.StpTxtEx = StpTxtEx
        self.RepTxtEx = RepTxtEx
        
    @property
    def StpTxtEx(self) -> str:
        return self.__StpTxtEx

    @StpTxtEx.setter
    def StpTxtEx(self, StpTxtEx: str):
        self.__StpTxtEx = StpTxtEx

    @property
    def RepTxtEx(self) -> str:
        return self.__RepTxtEx

    @RepTxtEx.setter
    def RepTxtEx(self, RepTxtEx: str):
        self.__RepTxtEx = RepTxtEx

class afpText_GSBMX(triplet):

    def __init__(self, MODE: str):
        self.MODE = MODE
        
    @property
    def MODE(self) -> str:
        return self.__MODE

    @MODE.setter
    def MODE(self, MODE: str):
        self.__MODE = MODE

class afpText_GSLT(triplet):

    def __init__(self, LINETYPE: str):
        self.LINETYPE = LINETYPE
        
    @property
    def LINETYPE(self) -> str:
        return self.__LINETYPE

    @LINETYPE.setter
    def LINETYPE(self, LINETYPE: str):
        self.__LINETYPE = LINETYPE

class afpText_ColorManagementResourceDescriptor(triplet):

    def __init__(self, ProcMode: str, CMRScpe: str):
        self.ProcMode = ProcMode
        self.CMRScpe = CMRScpe
        
    @property
    def ProcMode(self) -> str:
        return self.__ProcMode

    @ProcMode.setter
    def ProcMode(self, ProcMode: str):
        self.__ProcMode = ProcMode

    @property
    def CMRScpe(self) -> str:
        return self.__CMRScpe

    @CMRScpe.setter
    def CMRScpe(self, CMRScpe: str):
        self.__CMRScpe = CMRScpe

class afpText_GLINE(triplet):

    pass
class afpText_SamplingRatios(triplet):

    pass
class afpText_GPARC(triplet):

    def __init__(self, XPOS: str, YPOS: str, XCENT: str, YCENT: str, MH: str, MFR: str, START: str, SWEEP: str):
        self.XPOS = XPOS
        self.YPOS = YPOS
        self.XCENT = XCENT
        self.YCENT = YCENT
        self.MH = MH
        self.MFR = MFR
        self.START = START
        self.SWEEP = SWEEP
        
    @property
    def MFR(self) -> str:
        return self.__MFR

    @MFR.setter
    def MFR(self, MFR: str):
        self.__MFR = MFR

    @property
    def YCENT(self) -> str:
        return self.__YCENT

    @YCENT.setter
    def YCENT(self, YCENT: str):
        self.__YCENT = YCENT

    @property
    def SWEEP(self) -> str:
        return self.__SWEEP

    @SWEEP.setter
    def SWEEP(self, SWEEP: str):
        self.__SWEEP = SWEEP

    @property
    def START(self) -> str:
        return self.__START

    @START.setter
    def START(self, START: str):
        self.__START = START

    @property
    def XCENT(self) -> str:
        return self.__XCENT

    @XCENT.setter
    def XCENT(self, XCENT: str):
        self.__XCENT = XCENT

    @property
    def XPOS(self) -> str:
        return self.__XPOS

    @XPOS.setter
    def XPOS(self, XPOS: str):
        self.__XPOS = XPOS

    @property
    def YPOS(self) -> str:
        return self.__YPOS

    @YPOS.setter
    def YPOS(self, YPOS: str):
        self.__YPOS = YPOS

    @property
    def MH(self) -> str:
        return self.__MH

    @MH.setter
    def MH(self, MH: str):
        self.__MH = MH

class afpText_GEIMG(triplet):

    def __init__(self, DATA: str):
        self.DATA = DATA
        
    @property
    def DATA(self) -> str:
        return self.__DATA

    @DATA.setter
    def DATA(self, DATA: str):
        self.__DATA = DATA

class afpText_GSFLW(triplet):

    def __init__(self, MH: str, MFR: str):
        self.MH = MH
        self.MFR = MFR
        
    @property
    def MFR(self) -> str:
        return self.__MFR

    @MFR.setter
    def MFR(self, MFR: str):
        self.__MFR = MFR

    @property
    def MH(self) -> str:
        return self.__MH

    @MH.setter
    def MH(self, MH: str):
        self.__MH = MH

class afpText_PresentationControl(triplet):

    def __init__(self, PRSFlg: str):
        self.PRSFlg = PRSFlg
        
    @property
    def PRSFlg(self) -> str:
        return self.__PRSFlg

    @PRSFlg.setter
    def PRSFlg(self, PRSFlg: str):
        self.__PRSFlg = PRSFlg

class afpText_GSCR(triplet):

    def __init__(self, PREC: str):
        self.PREC = PREC
        
    @property
    def PREC(self) -> str:
        return self.__PREC

    @PREC.setter
    def PREC(self, PREC: str):
        self.__PREC = PREC

class afpText_GCFLT(triplet):

    pass
class afpText_FinishingOperation(triplet):

    def __init__(self, FOpType: str, RefEdge: str, FOpCnt: str, AxOffst: str, OpPos: str):
        self.FOpType = FOpType
        self.RefEdge = RefEdge
        self.FOpCnt = FOpCnt
        self.AxOffst = AxOffst
        self.OpPos = OpPos
        
    @property
    def FOpType(self) -> str:
        return self.__FOpType

    @FOpType.setter
    def FOpType(self, FOpType: str):
        self.__FOpType = FOpType

    @property
    def RefEdge(self) -> str:
        return self.__RefEdge

    @RefEdge.setter
    def RefEdge(self, RefEdge: str):
        self.__RefEdge = RefEdge

    @property
    def FOpCnt(self) -> str:
        return self.__FOpCnt

    @FOpCnt.setter
    def FOpCnt(self, FOpCnt: str):
        self.__FOpCnt = FOpCnt

    @property
    def AxOffst(self) -> str:
        return self.__AxOffst

    @AxOffst.setter
    def AxOffst(self, AxOffst: str):
        self.__AxOffst = AxOffst

    @property
    def OpPos(self) -> str:
        return self.__OpPos

    @OpPos.setter
    def OpPos(self, OpPos: str):
        self.__OpPos = OpPos

class afpText_GSLJ(triplet):

    def __init__(self, LINEJOIN: str):
        self.LINEJOIN = LINEJOIN
        
    @property
    def LINEJOIN(self) -> str:
        return self.__LINEJOIN

    @LINEJOIN.setter
    def LINEJOIN(self, LINEJOIN: str):
        self.__LINEJOIN = LINEJOIN

class afpText_SBI(triplet):

    def __init__(self, INCRMENT: str):
        self.INCRMENT = INCRMENT
        
    @property
    def INCRMENT(self) -> str:
        return self.__INCRMENT

    @INCRMENT.setter
    def INCRMENT(self, INCRMENT: str):
        self.__INCRMENT = INCRMENT

class afpText_GSPT(triplet):

    def __init__(self, PATT: str):
        self.PATT = PATT
        
    @property
    def PATT(self) -> str:
        return self.__PATT

    @PATT.setter
    def PATT(self, PATT: str):
        self.__PATT = PATT

class afpText_ResourceUsageAttribute(triplet):

    def __init__(self, Frequency: str):
        self.Frequency = Frequency
        
    @property
    def Frequency(self) -> str:
        return self.__Frequency

    @Frequency.setter
    def Frequency(self, Frequency: str):
        self.__Frequency = Frequency

class afpText_MeasurementUnits(triplet):

    def __init__(self, XoaBase: str, YoaBase: str, XoaUnits: str, YoaUnits: str):
        self.XoaBase = XoaBase
        self.YoaBase = YoaBase
        self.XoaUnits = XoaUnits
        self.YoaUnits = YoaUnits
        
    @property
    def YoaUnits(self) -> str:
        return self.__YoaUnits

    @YoaUnits.setter
    def YoaUnits(self, YoaUnits: str):
        self.__YoaUnits = YoaUnits

    @property
    def XoaUnits(self) -> str:
        return self.__XoaUnits

    @XoaUnits.setter
    def XoaUnits(self, XoaUnits: str):
        self.__XoaUnits = XoaUnits

    @property
    def XoaBase(self) -> str:
        return self.__XoaBase

    @XoaBase.setter
    def XoaBase(self, XoaBase: str):
        self.__XoaBase = XoaBase

    @property
    def YoaBase(self) -> str:
        return self.__YoaBase

    @YoaBase.setter
    def YoaBase(self, YoaBase: str):
        self.__YoaBase = YoaBase

class afpText_ObjectByteExtent(triplet):

    def __init__(self, ByteExt: str, ByteExtHi: str):
        self.ByteExt = ByteExt
        self.ByteExtHi = ByteExtHi
        
    @property
    def ByteExtHi(self) -> str:
        return self.__ByteExtHi

    @ByteExtHi.setter
    def ByteExtHi(self, ByteExtHi: str):
        self.__ByteExtHi = ByteExtHi

    @property
    def ByteExt(self) -> str:
        return self.__ByteExt

    @ByteExt.setter
    def ByteExt(self, ByteExt: str):
        self.__ByteExt = ByteExt

class afpText_TRN(triplet):

    def __init__(self, TRNDATA: str):
        self.TRNDATA = TRNDATA
        
    @property
    def TRNDATA(self) -> str:
        return self.__TRNDATA

    @TRNDATA.setter
    def TRNDATA(self, TRNDATA: str):
        self.__TRNDATA = TRNDATA

class afpText_GCHST(triplet):

    def __init__(self, XPOS: str, YPOS: str, CP: str):
        self.XPOS = XPOS
        self.YPOS = YPOS
        self.CP = CP
        
    @property
    def XPOS(self) -> str:
        return self.__XPOS

    @XPOS.setter
    def XPOS(self, XPOS: str):
        self.__XPOS = XPOS

    @property
    def YPOS(self) -> str:
        return self.__YPOS

    @YPOS.setter
    def YPOS(self, YPOS: str):
        self.__YPOS = YPOS

    @property
    def CP(self) -> str:
        return self.__CP

    @CP.setter
    def CP(self, CP: str):
        self.__CP = CP

class afpText_GSMP(triplet):

    def __init__(self, PREC: str):
        self.PREC = PREC
        
    @property
    def PREC(self) -> str:
        return self.__PREC

    @PREC.setter
    def PREC(self, PREC: str):
        self.__PREC = PREC

class afpText_GSCA(triplet):

    def __init__(self, XPOS: str, YPOS: str):
        self.XPOS = XPOS
        self.YPOS = YPOS
        
    @property
    def YPOS(self) -> str:
        return self.__YPOS

    @YPOS.setter
    def YPOS(self, YPOS: str):
        self.__YPOS = YPOS

    @property
    def XPOS(self) -> str:
        return self.__XPOS

    @XPOS.setter
    def XPOS(self, XPOS: str):
        self.__XPOS = XPOS

class afpText_IDEStructure(triplet):

    def __init__(self, FLAGS: str, FORMAT: str, SIZE1: str, SIZE2: str, SIZE3: str, SIZE4: str):
        self.FLAGS = FLAGS
        self.FORMAT = FORMAT
        self.SIZE1 = SIZE1
        self.SIZE2 = SIZE2
        self.SIZE3 = SIZE3
        self.SIZE4 = SIZE4
        
    @property
    def SIZE3(self) -> str:
        return self.__SIZE3

    @SIZE3.setter
    def SIZE3(self, SIZE3: str):
        self.__SIZE3 = SIZE3

    @property
    def SIZE2(self) -> str:
        return self.__SIZE2

    @SIZE2.setter
    def SIZE2(self, SIZE2: str):
        self.__SIZE2 = SIZE2

    @property
    def FLAGS(self) -> str:
        return self.__FLAGS

    @FLAGS.setter
    def FLAGS(self, FLAGS: str):
        self.__FLAGS = FLAGS

    @property
    def SIZE1(self) -> str:
        return self.__SIZE1

    @SIZE1.setter
    def SIZE1(self, SIZE1: str):
        self.__SIZE1 = SIZE1

    @property
    def SIZE4(self) -> str:
        return self.__SIZE4

    @SIZE4.setter
    def SIZE4(self, SIZE4: str):
        self.__SIZE4 = SIZE4

    @property
    def FORMAT(self) -> str:
        return self.__FORMAT

    @FORMAT.setter
    def FORMAT(self, FORMAT: str):
        self.__FORMAT = FORMAT

class afpText_DataObjectFontDescriptor(triplet):

    def __init__(self, FontTech: str, VFS: str, HFS: str, CharRot: str, EncEnv: str, EncID: str, Reserved: str, DOFtFlgs: str):
        self.FontTech = FontTech
        self.VFS = VFS
        self.HFS = HFS
        self.CharRot = CharRot
        self.EncEnv = EncEnv
        self.EncID = EncID
        self.Reserved = Reserved
        self.DOFtFlgs = DOFtFlgs
        
    @property
    def FontTech(self) -> str:
        return self.__FontTech

    @FontTech.setter
    def FontTech(self, FontTech: str):
        self.__FontTech = FontTech

    @property
    def CharRot(self) -> str:
        return self.__CharRot

    @CharRot.setter
    def CharRot(self, CharRot: str):
        self.__CharRot = CharRot

    @property
    def HFS(self) -> str:
        return self.__HFS

    @HFS.setter
    def HFS(self, HFS: str):
        self.__HFS = HFS

    @property
    def Reserved(self) -> str:
        return self.__Reserved

    @Reserved.setter
    def Reserved(self, Reserved: str):
        self.__Reserved = Reserved

    @property
    def VFS(self) -> str:
        return self.__VFS

    @VFS.setter
    def VFS(self, VFS: str):
        self.__VFS = VFS

    @property
    def EncID(self) -> str:
        return self.__EncID

    @EncID.setter
    def EncID(self, EncID: str):
        self.__EncID = EncID

    @property
    def EncEnv(self) -> str:
        return self.__EncEnv

    @EncEnv.setter
    def EncEnv(self, EncEnv: str):
        self.__EncEnv = EncEnv

    @property
    def DOFtFlgs(self) -> str:
        return self.__DOFtFlgs

    @DOFtFlgs.setter
    def DOFtFlgs(self, DOFtFlgs: str):
        self.__DOFtFlgs = DOFtFlgs

class afpText_LocalDateAndTimeStamp(triplet):

    def __init__(self, TenYear: str, Day: str, Hour: str, Minute: str, Second: str, HundSec: str, StampType: str, THunYear: str):
        self.TenYear = TenYear
        self.Day = Day
        self.Hour = Hour
        self.Minute = Minute
        self.Second = Second
        self.HundSec = HundSec
        self.StampType = StampType
        self.THunYear = THunYear
        
    @property
    def Second(self) -> str:
        return self.__Second

    @Second.setter
    def Second(self, Second: str):
        self.__Second = Second

    @property
    def THunYear(self) -> str:
        return self.__THunYear

    @THunYear.setter
    def THunYear(self, THunYear: str):
        self.__THunYear = THunYear

    @property
    def HundSec(self) -> str:
        return self.__HundSec

    @HundSec.setter
    def HundSec(self, HundSec: str):
        self.__HundSec = HundSec

    @property
    def Day(self) -> str:
        return self.__Day

    @Day.setter
    def Day(self, Day: str):
        self.__Day = Day

    @property
    def Minute(self) -> str:
        return self.__Minute

    @Minute.setter
    def Minute(self, Minute: str):
        self.__Minute = Minute

    @property
    def StampType(self) -> str:
        return self.__StampType

    @StampType.setter
    def StampType(self, StampType: str):
        self.__StampType = StampType

    @property
    def TenYear(self) -> str:
        return self.__TenYear

    @TenYear.setter
    def TenYear(self, TenYear: str):
        self.__TenYear = TenYear

    @property
    def Hour(self) -> str:
        return self.__Hour

    @Hour.setter
    def Hour(self, Hour: str):
        self.__Hour = Hour

class afpText_GBIMG(triplet):

    def __init__(self, XPOS: str, YPOS: str, FORMAT: str, RES: str, WIDTH: str, HEIGHT: str):
        self.XPOS = XPOS
        self.YPOS = YPOS
        self.FORMAT = FORMAT
        self.RES = RES
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        
    @property
    def RES(self) -> str:
        return self.__RES

    @RES.setter
    def RES(self, RES: str):
        self.__RES = RES

    @property
    def HEIGHT(self) -> str:
        return self.__HEIGHT

    @HEIGHT.setter
    def HEIGHT(self, HEIGHT: str):
        self.__HEIGHT = HEIGHT

    @property
    def YPOS(self) -> str:
        return self.__YPOS

    @YPOS.setter
    def YPOS(self, YPOS: str):
        self.__YPOS = YPOS

    @property
    def WIDTH(self) -> str:
        return self.__WIDTH

    @WIDTH.setter
    def WIDTH(self, WIDTH: str):
        self.__WIDTH = WIDTH

    @property
    def FORMAT(self) -> str:
        return self.__FORMAT

    @FORMAT.setter
    def FORMAT(self, FORMAT: str):
        self.__FORMAT = FORMAT

    @property
    def XPOS(self) -> str:
        return self.__XPOS

    @XPOS.setter
    def XPOS(self, XPOS: str):
        self.__XPOS = XPOS

class afpText_ObjectCount(triplet):

    def __init__(self, SubObj: str, SObjNum: str, SobjNmHi: str):
        self.SubObj = SubObj
        self.SObjNum = SObjNum
        self.SobjNmHi = SobjNmHi
        
    @property
    def SobjNmHi(self) -> str:
        return self.__SobjNmHi

    @SobjNmHi.setter
    def SobjNmHi(self, SobjNmHi: str):
        self.__SobjNmHi = SobjNmHi

    @property
    def SObjNum(self) -> str:
        return self.__SObjNum

    @SObjNum.setter
    def SObjNum(self, SObjNum: str):
        self.__SObjNum = SObjNum

    @property
    def SubObj(self) -> str:
        return self.__SubObj

    @SubObj.setter
    def SubObj(self, SubObj: str):
        self.__SubObj = SubObj

class afpText_ImageSize(triplet):

    def __init__(self, UNITBASE: str, HRESOL: str, VRESOL: str, HSIZE: str, VSIZE: str):
        self.UNITBASE = UNITBASE
        self.HRESOL = HRESOL
        self.VRESOL = VRESOL
        self.HSIZE = HSIZE
        self.VSIZE = VSIZE
        
    @property
    def HSIZE(self) -> str:
        return self.__HSIZE

    @HSIZE.setter
    def HSIZE(self, HSIZE: str):
        self.__HSIZE = HSIZE

    @property
    def VSIZE(self) -> str:
        return self.__VSIZE

    @VSIZE.setter
    def VSIZE(self, VSIZE: str):
        self.__VSIZE = VSIZE

    @property
    def HRESOL(self) -> str:
        return self.__HRESOL

    @HRESOL.setter
    def HRESOL(self, HRESOL: str):
        self.__HRESOL = HRESOL

    @property
    def UNITBASE(self) -> str:
        return self.__UNITBASE

    @UNITBASE.setter
    def UNITBASE(self, UNITBASE: str):
        self.__UNITBASE = UNITBASE

    @property
    def VRESOL(self) -> str:
        return self.__VRESOL

    @VRESOL.setter
    def VRESOL(self, VRESOL: str):
        self.__VRESOL = VRESOL

class afpText_GRLINE(triplet):

    def __init__(self, XPOS: str, YPOS: str, afpText_GRLINE: set["afpText_GRLINERG"] = None):
        self.XPOS = XPOS
        self.YPOS = YPOS
        self.afpText_GRLINE = afpText_GRLINE if afpText_GRLINE is not None else set()
        
    @property
    def YPOS(self) -> str:
        return self.__YPOS

    @YPOS.setter
    def YPOS(self, YPOS: str):
        self.__YPOS = YPOS

    @property
    def XPOS(self) -> str:
        return self.__XPOS

    @XPOS.setter
    def XPOS(self, XPOS: str):
        self.__XPOS = XPOS

    @property
    def afpText_GRLINE(self):
        return self.__afpText_GRLINE

    @afpText_GRLINE.setter
    def afpText_GRLINE(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_GRLINE__afpText_GRLINE", None)
        self.__afpText_GRLINE = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_GRLINERG"):
                    opp_val = getattr(item, "afpText_GRLINERG", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_GRLINERG", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_GRLINERG"):
                    opp_val = getattr(item, "afpText_GRLINERG", None)
                    
                    setattr(item, "afpText_GRLINERG", self)
                    

class afpText_BandImageData(triplet):

    def __init__(self, BANDNUM: str, RESERVED: str, DATA: str):
        self.BANDNUM = BANDNUM
        self.RESERVED = RESERVED
        self.DATA = DATA
        
    @property
    def DATA(self) -> str:
        return self.__DATA

    @DATA.setter
    def DATA(self, DATA: str):
        self.__DATA = DATA

    @property
    def RESERVED(self) -> str:
        return self.__RESERVED

    @RESERVED.setter
    def RESERVED(self, RESERVED: str):
        self.__RESERVED = RESERVED

    @property
    def BANDNUM(self) -> str:
        return self.__BANDNUM

    @BANDNUM.setter
    def BANDNUM(self, BANDNUM: str):
        self.__BANDNUM = BANDNUM

class afpText_GCCHST(triplet):

    def __init__(self, CP: str):
        self.CP = CP
        
    @property
    def CP(self) -> str:
        return self.__CP

    @CP.setter
    def CP(self, CP: str):
        self.__CP = CP

class afpText_GCLINE(triplet):

    pass
class afpText_ImageEncoding(triplet):

    def __init__(self, COMPRID: str, RECID: str, BITORDR: str):
        self.COMPRID = COMPRID
        self.RECID = RECID
        self.BITORDR = BITORDR
        
    @property
    def RECID(self) -> str:
        return self.__RECID

    @RECID.setter
    def RECID(self, RECID: str):
        self.__RECID = RECID

    @property
    def COMPRID(self) -> str:
        return self.__COMPRID

    @COMPRID.setter
    def COMPRID(self, COMPRID: str):
        self.__COMPRID = COMPRID

    @property
    def BITORDR(self) -> str:
        return self.__BITORDR

    @BITORDR.setter
    def BITORDR(self, BITORDR: str):
        self.__BITORDR = BITORDR

class afpText_WindowSpecification(triplet):

    def __init__(self, IMGXYRES: str, XLWIND: str, XRWIND: str, YBWIND: str, YTWIND: str, FLAGS: str, RES3: str, CFORMAT: str, UBASE: str, XRESOL: str, YRESOL: str):
        self.IMGXYRES = IMGXYRES
        self.XLWIND = XLWIND
        self.XRWIND = XRWIND
        self.YBWIND = YBWIND
        self.YTWIND = YTWIND
        self.FLAGS = FLAGS
        self.RES3 = RES3
        self.CFORMAT = CFORMAT
        self.UBASE = UBASE
        self.XRESOL = XRESOL
        self.YRESOL = YRESOL
        
    @property
    def YRESOL(self) -> str:
        return self.__YRESOL

    @YRESOL.setter
    def YRESOL(self, YRESOL: str):
        self.__YRESOL = YRESOL

    @property
    def YBWIND(self) -> str:
        return self.__YBWIND

    @YBWIND.setter
    def YBWIND(self, YBWIND: str):
        self.__YBWIND = YBWIND

    @property
    def XLWIND(self) -> str:
        return self.__XLWIND

    @XLWIND.setter
    def XLWIND(self, XLWIND: str):
        self.__XLWIND = XLWIND

    @property
    def FLAGS(self) -> str:
        return self.__FLAGS

    @FLAGS.setter
    def FLAGS(self, FLAGS: str):
        self.__FLAGS = FLAGS

    @property
    def UBASE(self) -> str:
        return self.__UBASE

    @UBASE.setter
    def UBASE(self, UBASE: str):
        self.__UBASE = UBASE

    @property
    def YTWIND(self) -> str:
        return self.__YTWIND

    @YTWIND.setter
    def YTWIND(self, YTWIND: str):
        self.__YTWIND = YTWIND

    @property
    def IMGXYRES(self) -> str:
        return self.__IMGXYRES

    @IMGXYRES.setter
    def IMGXYRES(self, IMGXYRES: str):
        self.__IMGXYRES = IMGXYRES

    @property
    def XRWIND(self) -> str:
        return self.__XRWIND

    @XRWIND.setter
    def XRWIND(self, XRWIND: str):
        self.__XRWIND = XRWIND

    @property
    def RES3(self) -> str:
        return self.__RES3

    @RES3.setter
    def RES3(self, RES3: str):
        self.__RES3 = RES3

    @property
    def XRESOL(self) -> str:
        return self.__XRESOL

    @XRESOL.setter
    def XRESOL(self, XRESOL: str):
        self.__XRESOL = XRESOL

    @property
    def CFORMAT(self) -> str:
        return self.__CFORMAT

    @CFORMAT.setter
    def CFORMAT(self, CFORMAT: str):
        self.__CFORMAT = CFORMAT

class afpText_FontResolution(triplet):

    def __init__(self, MetTech: str, RPuBase: str, RPUnits: str):
        self.MetTech = MetTech
        self.RPuBase = RPuBase
        self.RPUnits = RPUnits
        
    @property
    def RPUnits(self) -> str:
        return self.__RPUnits

    @RPUnits.setter
    def RPUnits(self, RPUnits: str):
        self.__RPUnits = RPUnits

    @property
    def MetTech(self) -> str:
        return self.__MetTech

    @MetTech.setter
    def MetTech(self, MetTech: str):
        self.__MetTech = MetTech

    @property
    def RPuBase(self) -> str:
        return self.__RPuBase

    @RPuBase.setter
    def RPuBase(self, RPuBase: str):
        self.__RPuBase = RPuBase

class afpText_ResourceObjectInclude(triplet):

    def __init__(self, ObjType: str, ObjName: str, XobjOset: str, YobjOset: str, ObOrent: str):
        self.ObjType = ObjType
        self.ObjName = ObjName
        self.XobjOset = XobjOset
        self.YobjOset = YobjOset
        self.ObOrent = ObOrent
        
    @property
    def XobjOset(self) -> str:
        return self.__XobjOset

    @XobjOset.setter
    def XobjOset(self, XobjOset: str):
        self.__XobjOset = XobjOset

    @property
    def ObOrent(self) -> str:
        return self.__ObOrent

    @ObOrent.setter
    def ObOrent(self, ObOrent: str):
        self.__ObOrent = ObOrent

    @property
    def ObjType(self) -> str:
        return self.__ObjType

    @ObjType.setter
    def ObjType(self, ObjType: str):
        self.__ObjType = ObjType

    @property
    def ObjName(self) -> str:
        return self.__ObjName

    @ObjName.setter
    def ObjName(self, ObjName: str):
        self.__ObjName = ObjName

    @property
    def YobjOset(self) -> str:
        return self.__YobjOset

    @YobjOset.setter
    def YobjOset(self, YobjOset: str):
        self.__YobjOset = YobjOset

class afpText_MediaFidelity(triplet):

    def __init__(self, StpMedEx: str, Reserved: str):
        self.StpMedEx = StpMedEx
        self.Reserved = Reserved
        
    @property
    def Reserved(self) -> str:
        return self.__Reserved

    @Reserved.setter
    def Reserved(self, Reserved: str):
        self.__Reserved = Reserved

    @property
    def StpMedEx(self) -> str:
        return self.__StpMedEx

    @StpMedEx.setter
    def StpMedEx(self, StpMedEx: str):
        self.__StpMedEx = StpMedEx

class afpText_LocaleSelector(triplet):

    def __init__(self, LocFlgs: str, LangCode: str, ScrptCde: str, RegCde: str, Reserved: str, VarCde: str):
        self.LocFlgs = LocFlgs
        self.LangCode = LangCode
        self.ScrptCde = ScrptCde
        self.RegCde = RegCde
        self.Reserved = Reserved
        self.VarCde = VarCde
        
    @property
    def LocFlgs(self) -> str:
        return self.__LocFlgs

    @LocFlgs.setter
    def LocFlgs(self, LocFlgs: str):
        self.__LocFlgs = LocFlgs

    @property
    def LangCode(self) -> str:
        return self.__LangCode

    @LangCode.setter
    def LangCode(self, LangCode: str):
        self.__LangCode = LangCode

    @property
    def Reserved(self) -> str:
        return self.__Reserved

    @Reserved.setter
    def Reserved(self, Reserved: str):
        self.__Reserved = Reserved

    @property
    def RegCde(self) -> str:
        return self.__RegCde

    @RegCde.setter
    def RegCde(self, RegCde: str):
        self.__RegCde = RegCde

    @property
    def ScrptCde(self) -> str:
        return self.__ScrptCde

    @ScrptCde.setter
    def ScrptCde(self, ScrptCde: str):
        self.__ScrptCde = ScrptCde

    @property
    def VarCde(self) -> str:
        return self.__VarCde

    @VarCde.setter
    def VarCde(self, VarCde: str):
        self.__VarCde = VarCde

class afpText_OVS(triplet):

    def __init__(self, BYPSIDEN: str, OVERCHAR: str):
        self.BYPSIDEN = BYPSIDEN
        self.OVERCHAR = OVERCHAR
        
    @property
    def BYPSIDEN(self) -> str:
        return self.__BYPSIDEN

    @BYPSIDEN.setter
    def BYPSIDEN(self, BYPSIDEN: str):
        self.__BYPSIDEN = BYPSIDEN

    @property
    def OVERCHAR(self) -> str:
        return self.__OVERCHAR

    @OVERCHAR.setter
    def OVERCHAR(self, OVERCHAR: str):
        self.__OVERCHAR = OVERCHAR

class afpText_ResourceObjectType(triplet):

    def __init__(self, ObjType: str, ConData: str):
        self.ObjType = ObjType
        self.ConData = ConData
        
    @property
    def ConData(self) -> str:
        return self.__ConData

    @ConData.setter
    def ConData(self, ConData: str):
        self.__ConData = ConData

    @property
    def ObjType(self) -> str:
        return self.__ObjType

    @ObjType.setter
    def ObjType(self, ObjType: str):
        self.__ObjType = ObjType

class afpText_PagePositionInformation(triplet):

    def __init__(self, PGPRG: str):
        self.PGPRG = PGPRG
        
    @property
    def PGPRG(self) -> str:
        return self.__PGPRG

    @PGPRG.setter
    def PGPRG(self, PGPRG: str):
        self.__PGPRG = PGPRG

class afpText_DIR(triplet):

    def __init__(self, RLENGTH: str, RWIDTH: str, RWIDTHFRACTION: str):
        self.RLENGTH = RLENGTH
        self.RWIDTH = RWIDTH
        self.RWIDTHFRACTION = RWIDTHFRACTION
        
    @property
    def RWIDTHFRACTION(self) -> str:
        return self.__RWIDTHFRACTION

    @RWIDTHFRACTION.setter
    def RWIDTHFRACTION(self, RWIDTHFRACTION: str):
        self.__RWIDTHFRACTION = RWIDTHFRACTION

    @property
    def RLENGTH(self) -> str:
        return self.__RLENGTH

    @RLENGTH.setter
    def RLENGTH(self, RLENGTH: str):
        self.__RLENGTH = RLENGTH

    @property
    def RWIDTH(self) -> str:
        return self.__RWIDTH

    @RWIDTH.setter
    def RWIDTH(self, RWIDTH: str):
        self.__RWIDTH = RWIDTH

class afpText_DBR(triplet):

    def __init__(self, RLENGTH: str, RWIDTH: str, RWIDTHFRACTION: str):
        self.RLENGTH = RLENGTH
        self.RWIDTH = RWIDTH
        self.RWIDTHFRACTION = RWIDTHFRACTION
        
    @property
    def RWIDTHFRACTION(self) -> str:
        return self.__RWIDTHFRACTION

    @RWIDTHFRACTION.setter
    def RWIDTHFRACTION(self, RWIDTHFRACTION: str):
        self.__RWIDTHFRACTION = RWIDTHFRACTION

    @property
    def RWIDTH(self) -> str:
        return self.__RWIDTH

    @RWIDTH.setter
    def RWIDTH(self, RWIDTH: str):
        self.__RWIDTH = RWIDTH

    @property
    def RLENGTH(self) -> str:
        return self.__RLENGTH

    @RLENGTH.setter
    def RLENGTH(self, RLENGTH: str):
        self.__RLENGTH = RLENGTH

class afpText_GSLW(triplet):

    def __init__(self, MH: str):
        self.MH = MH
        
    @property
    def MH(self) -> str:
        return self.__MH

    @MH.setter
    def MH(self, MH: str):
        self.__MH = MH

class afpText_TextOrientation(triplet):

    def __init__(self, IAxis: str, BAxis: str):
        self.IAxis = IAxis
        self.BAxis = BAxis
        
    @property
    def IAxis(self) -> str:
        return self.__IAxis

    @IAxis.setter
    def IAxis(self, IAxis: str):
        self.__IAxis = IAxis

    @property
    def BAxis(self) -> str:
        return self.__BAxis

    @BAxis.setter
    def BAxis(self, BAxis: str):
        self.__BAxis = BAxis

class afpText_GMRK(triplet):

    pass
class afpText_GSPS(triplet):

    def __init__(self, LCID: str):
        self.LCID = LCID
        
    @property
    def LCID(self) -> str:
        return self.__LCID

    @LCID.setter
    def LCID(self, LCID: str):
        self.__LCID = LCID

class afpText_GSAP(triplet):

    def __init__(self, S: str, P: str, Q: str, R: str):
        self.S = S
        self.P = P
        self.Q = Q
        self.R = R
        
    @property
    def S(self) -> str:
        return self.__S

    @S.setter
    def S(self, S: str):
        self.__S = S

    @property
    def P(self) -> str:
        return self.__P

    @P.setter
    def P(self, P: str):
        self.__P = P

    @property
    def Q(self) -> str:
        return self.__Q

    @Q.setter
    def Q(self, Q: str):
        self.__Q = Q

    @property
    def R(self) -> str:
        return self.__R

    @R.setter
    def R(self, R: str):
        self.__R = R

class afpText_TileSize(triplet):

    def __init__(self, THSIZE: str, TVSIZE: str, RELRES: str):
        self.THSIZE = THSIZE
        self.TVSIZE = TVSIZE
        self.RELRES = RELRES
        
    @property
    def THSIZE(self) -> str:
        return self.__THSIZE

    @THSIZE.setter
    def THSIZE(self, THSIZE: str):
        self.__THSIZE = THSIZE

    @property
    def TVSIZE(self) -> str:
        return self.__TVSIZE

    @TVSIZE.setter
    def TVSIZE(self, TVSIZE: str):
        self.__TVSIZE = TVSIZE

    @property
    def RELRES(self) -> str:
        return self.__RELRES

    @RELRES.setter
    def RELRES(self, RELRES: str):
        self.__RELRES = RELRES

class afpText_ExternalAlgorithm(triplet):

    def __init__(self, ALGTYPE: str, afpText_ExternalAlgorithm: set["afpText_ExternalAlgorithmRG"] = None):
        self.ALGTYPE = ALGTYPE
        self.afpText_ExternalAlgorithm = afpText_ExternalAlgorithm if afpText_ExternalAlgorithm is not None else set()
        
    @property
    def ALGTYPE(self) -> str:
        return self.__ALGTYPE

    @ALGTYPE.setter
    def ALGTYPE(self, ALGTYPE: str):
        self.__ALGTYPE = ALGTYPE

    @property
    def afpText_ExternalAlgorithm(self):
        return self.__afpText_ExternalAlgorithm

    @afpText_ExternalAlgorithm.setter
    def afpText_ExternalAlgorithm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_ExternalAlgorithm__afpText_ExternalAlgorithm", None)
        self.__afpText_ExternalAlgorithm = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_ExternalAlgorithmRG"):
                    opp_val = getattr(item, "afpText_ExternalAlgorithmRG", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_ExternalAlgorithmRG", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_ExternalAlgorithmRG"):
                    opp_val = getattr(item, "afpText_ExternalAlgorithmRG", None)
                    
                    setattr(item, "afpText_ExternalAlgorithmRG", self)
                    

class afpText_AttributeValue(triplet):

    def __init__(self, Reserved0: str, AttVal: str):
        self.Reserved0 = Reserved0
        self.AttVal = AttVal
        
    @property
    def Reserved0(self) -> str:
        return self.__Reserved0

    @Reserved0.setter
    def Reserved0(self, Reserved0: str):
        self.__Reserved0 = Reserved0

    @property
    def AttVal(self) -> str:
        return self.__AttVal

    @AttVal.setter
    def AttVal(self, AttVal: str):
        self.__AttVal = AttVal

class afpText_GSMX(triplet):

    def __init__(self, MODE: str):
        self.MODE = MODE
        
    @property
    def MODE(self) -> str:
        return self.__MODE

    @MODE.setter
    def MODE(self, MODE: str):
        self.__MODE = MODE

class afpText_GIMD(triplet):

    def __init__(self, DATA: str):
        self.DATA = DATA
        
    @property
    def DATA(self) -> str:
        return self.__DATA

    @DATA.setter
    def DATA(self, DATA: str):
        self.__DATA = DATA

class afpText_CGCSGID(triplet):

    def __init__(self, GCSGID: str, CPGID: str):
        self.GCSGID = GCSGID
        self.CPGID = CPGID
        
    @property
    def GCSGID(self) -> str:
        return self.__GCSGID

    @GCSGID.setter
    def GCSGID(self, GCSGID: str):
        self.__GCSGID = GCSGID

    @property
    def CPGID(self) -> str:
        return self.__CPGID

    @CPGID.setter
    def CPGID(self, CPGID: str):
        self.__CPGID = CPGID

class afpText_DrawingOrderSubset(triplet):

    pass
class afpText_FontHorizontalScaleFactor(triplet):

    def __init__(self, Hscale: str):
        self.Hscale = Hscale
        
    @property
    def Hscale(self) -> str:
        return self.__Hscale

    @Hscale.setter
    def Hscale(self, Hscale: str):
        self.__Hscale = Hscale

class afpText_USC(triplet):

    def __init__(self, BYPSIDEN: str):
        self.BYPSIDEN = BYPSIDEN
        
    @property
    def BYPSIDEN(self) -> str:
        return self.__BYPSIDEN

    @BYPSIDEN.setter
    def BYPSIDEN(self, BYPSIDEN: str):
        self.__BYPSIDEN = BYPSIDEN

class afpText_GNOP1(triplet):

    pass
class afpText_SVI(triplet):

    def __init__(self, INCRMENT: str):
        self.INCRMENT = INCRMENT
        
    @property
    def INCRMENT(self) -> str:
        return self.__INCRMENT

    @INCRMENT.setter
    def INCRMENT(self, INCRMENT: str):
        self.__INCRMENT = INCRMENT

class afpText_FontFidelity(triplet):

    def __init__(self, StpFntEx: str):
        self.StpFntEx = StpFntEx
        
    @property
    def StpFntEx(self) -> str:
        return self.__StpFntEx

    @StpFntEx.setter
    def StpFntEx(self, StpFntEx: str):
        self.__StpFntEx = StpFntEx

class afpText_ESU(triplet):

    def __init__(self, LID: str):
        self.LID = LID
        
    @property
    def LID(self) -> str:
        return self.__LID

    @LID.setter
    def LID(self, LID: str):
        self.__LID = LID

class afpText_TonerSaver(triplet):

    def __init__(self, TSvCtrl: str):
        self.TSvCtrl = TSvCtrl
        
    @property
    def TSvCtrl(self) -> str:
        return self.__TSvCtrl

    @TSvCtrl.setter
    def TSvCtrl(self, TSvCtrl: str):
        self.__TSvCtrl = TSvCtrl

class afpText_ObjectFunctionSetSpecification(triplet):

    def __init__(self, ObjType: str, ArchVrsn: str, DCAFnSet: str, OCAFnSet: str):
        self.ObjType = ObjType
        self.ArchVrsn = ArchVrsn
        self.DCAFnSet = DCAFnSet
        self.OCAFnSet = OCAFnSet
        
    @property
    def ArchVrsn(self) -> str:
        return self.__ArchVrsn

    @ArchVrsn.setter
    def ArchVrsn(self, ArchVrsn: str):
        self.__ArchVrsn = ArchVrsn

    @property
    def OCAFnSet(self) -> str:
        return self.__OCAFnSet

    @OCAFnSet.setter
    def OCAFnSet(self, OCAFnSet: str):
        self.__OCAFnSet = OCAFnSet

    @property
    def DCAFnSet(self) -> str:
        return self.__DCAFnSet

    @DCAFnSet.setter
    def DCAFnSet(self, DCAFnSet: str):
        self.__DCAFnSet = DCAFnSet

    @property
    def ObjType(self) -> str:
        return self.__ObjType

    @ObjType.setter
    def ObjType(self, ObjType: str):
        self.__ObjType = ObjType

class afpText_STO(triplet):

    def __init__(self, IORNTION: str, BORNTION: str):
        self.IORNTION = IORNTION
        self.BORNTION = BORNTION
        
    @property
    def BORNTION(self) -> str:
        return self.__BORNTION

    @BORNTION.setter
    def BORNTION(self, BORNTION: str):
        self.__BORNTION = BORNTION

    @property
    def IORNTION(self) -> str:
        return self.__IORNTION

    @IORNTION.setter
    def IORNTION(self, IORNTION: str):
        self.__IORNTION = IORNTION

class afpText_ImageSubsampling(triplet):

    pass
class afpText_SEC(triplet):

    def __init__(self, RESERVED: str, COLSPCE: str, COLSIZE1: str, COLSIZE2: str, COLSIZE3: str, COLSIZE4: str, COLVALUE: str):
        self.RESERVED = RESERVED
        self.COLSPCE = COLSPCE
        self.COLSIZE1 = COLSIZE1
        self.COLSIZE2 = COLSIZE2
        self.COLSIZE3 = COLSIZE3
        self.COLSIZE4 = COLSIZE4
        self.COLVALUE = COLVALUE
        
    @property
    def COLSIZE2(self) -> str:
        return self.__COLSIZE2

    @COLSIZE2.setter
    def COLSIZE2(self, COLSIZE2: str):
        self.__COLSIZE2 = COLSIZE2

    @property
    def RESERVED(self) -> str:
        return self.__RESERVED

    @RESERVED.setter
    def RESERVED(self, RESERVED: str):
        self.__RESERVED = RESERVED

    @property
    def COLSIZE4(self) -> str:
        return self.__COLSIZE4

    @COLSIZE4.setter
    def COLSIZE4(self, COLSIZE4: str):
        self.__COLSIZE4 = COLSIZE4

    @property
    def COLSIZE1(self) -> str:
        return self.__COLSIZE1

    @COLSIZE1.setter
    def COLSIZE1(self, COLSIZE1: str):
        self.__COLSIZE1 = COLSIZE1

    @property
    def COLSPCE(self) -> str:
        return self.__COLSPCE

    @COLSPCE.setter
    def COLSPCE(self, COLSPCE: str):
        self.__COLSPCE = COLSPCE

    @property
    def COLVALUE(self) -> str:
        return self.__COLVALUE

    @COLVALUE.setter
    def COLVALUE(self, COLVALUE: str):
        self.__COLVALUE = COLVALUE

    @property
    def COLSIZE3(self) -> str:
        return self.__COLSIZE3

    @COLSIZE3.setter
    def COLSIZE3(self, COLSIZE3: str):
        self.__COLSIZE3 = COLSIZE3

class afpText_FinishingFidelity(triplet):

    def __init__(self, StpFinEx: str, RepFinEx: str):
        self.StpFinEx = StpFinEx
        self.RepFinEx = RepFinEx
        
    @property
    def RepFinEx(self) -> str:
        return self.__RepFinEx

    @RepFinEx.setter
    def RepFinEx(self, RepFinEx: str):
        self.__RepFinEx = RepFinEx

    @property
    def StpFinEx(self) -> str:
        return self.__StpFinEx

    @StpFinEx.setter
    def StpFinEx(self, StpFinEx: str):
        self.__StpFinEx = StpFinEx

class afpText_SIA(triplet):

    def __init__(self, DIRCTION: str, ADJSTMNT: str):
        self.DIRCTION = DIRCTION
        self.ADJSTMNT = ADJSTMNT
        
    @property
    def ADJSTMNT(self) -> str:
        return self.__ADJSTMNT

    @ADJSTMNT.setter
    def ADJSTMNT(self, ADJSTMNT: str):
        self.__ADJSTMNT = ADJSTMNT

    @property
    def DIRCTION(self) -> str:
        return self.__DIRCTION

    @DIRCTION.setter
    def DIRCTION(self, DIRCTION: str):
        self.__DIRCTION = DIRCTION

class afpText_TileTOC(triplet):

    def __init__(self, Reserved: str, afpText_TileTOC: set["afpText_TileTOCRG"] = None):
        self.Reserved = Reserved
        self.afpText_TileTOC = afpText_TileTOC if afpText_TileTOC is not None else set()
        
    @property
    def Reserved(self) -> str:
        return self.__Reserved

    @Reserved.setter
    def Reserved(self, Reserved: str):
        self.__Reserved = Reserved

    @property
    def afpText_TileTOC(self):
        return self.__afpText_TileTOC

    @afpText_TileTOC.setter
    def afpText_TileTOC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_TileTOC__afpText_TileTOC", None)
        self.__afpText_TileTOC = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_TileTOCRG"):
                    opp_val = getattr(item, "afpText_TileTOCRG", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_TileTOCRG", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_TileTOCRG"):
                    opp_val = getattr(item, "afpText_TileTOCRG", None)
                    
                    setattr(item, "afpText_TileTOCRG", self)
                    

class afpText_BeginImage(triplet):

    def __init__(self, OBJTYPE: str):
        self.OBJTYPE = OBJTYPE
        
    @property
    def OBJTYPE(self) -> str:
        return self.__OBJTYPE

    @OBJTYPE.setter
    def OBJTYPE(self, OBJTYPE: str):
        self.__OBJTYPE = OBJTYPE

class afpText_MediumOrientation(triplet):

    def __init__(self, MedOrient: str):
        self.MedOrient = MedOrient
        
    @property
    def MedOrient(self) -> str:
        return self.__MedOrient

    @MedOrient.setter
    def MedOrient(self, MedOrient: str):
        self.__MedOrient = MedOrient

class afpText_GSCD(triplet):

    def __init__(self, DIRECTION: str):
        self.DIRECTION = DIRECTION
        
    @property
    def DIRECTION(self) -> str:
        return self.__DIRECTION

    @DIRECTION.setter
    def DIRECTION(self, DIRECTION: str):
        self.__DIRECTION = DIRECTION

class afpText_ImageLUTID(triplet):

    def __init__(self, LUTID: str):
        self.LUTID = LUTID
        
    @property
    def LUTID(self) -> str:
        return self.__LUTID

    @LUTID.setter
    def LUTID(self, LUTID: str):
        self.__LUTID = LUTID

class afpText_GFARC(triplet):

    def __init__(self, XPOS: str, YPOS: str, MH: str, MFR: str):
        self.XPOS = XPOS
        self.YPOS = YPOS
        self.MH = MH
        self.MFR = MFR
        
    @property
    def XPOS(self) -> str:
        return self.__XPOS

    @XPOS.setter
    def XPOS(self, XPOS: str):
        self.__XPOS = XPOS

    @property
    def MFR(self) -> str:
        return self.__MFR

    @MFR.setter
    def MFR(self, MFR: str):
        self.__MFR = MFR

    @property
    def YPOS(self) -> str:
        return self.__YPOS

    @YPOS.setter
    def YPOS(self, YPOS: str):
        self.__YPOS = YPOS

    @property
    def MH(self) -> str:
        return self.__MH

    @MH.setter
    def MH(self, MH: str):
        self.__MH = MH

class afpText_GCPARC(triplet):

    def __init__(self, XCENT: str, YCENT: str, MH: str, MFR: str, START: str, SWEEP: str):
        self.XCENT = XCENT
        self.YCENT = YCENT
        self.MH = MH
        self.MFR = MFR
        self.START = START
        self.SWEEP = SWEEP
        
    @property
    def XCENT(self) -> str:
        return self.__XCENT

    @XCENT.setter
    def XCENT(self, XCENT: str):
        self.__XCENT = XCENT

    @property
    def YCENT(self) -> str:
        return self.__YCENT

    @YCENT.setter
    def YCENT(self, YCENT: str):
        self.__YCENT = YCENT

    @property
    def MFR(self) -> str:
        return self.__MFR

    @MFR.setter
    def MFR(self, MFR: str):
        self.__MFR = MFR

    @property
    def MH(self) -> str:
        return self.__MH

    @MH.setter
    def MH(self, MH: str):
        self.__MH = MH

    @property
    def SWEEP(self) -> str:
        return self.__SWEEP

    @SWEEP.setter
    def SWEEP(self, SWEEP: str):
        self.__SWEEP = SWEEP

    @property
    def START(self) -> str:
        return self.__START

    @START.setter
    def START(self, START: str):
        self.__START = START

class afpText_ResourceSectionNumber(triplet):

    def __init__(self, ResSNum: str):
        self.ResSNum = ResSNum
        
    @property
    def ResSNum(self) -> str:
        return self.__ResSNum

    @ResSNum.setter
    def ResSNum(self, ResSNum: str):
        self.__ResSNum = ResSNum

class afpText_ObjectOffset(triplet):

    def __init__(self, ObjTpe: str, ObjOset: str, ObjOstHi: str):
        self.ObjTpe = ObjTpe
        self.ObjOset = ObjOset
        self.ObjOstHi = ObjOstHi
        
    @property
    def ObjOstHi(self) -> str:
        return self.__ObjOstHi

    @ObjOstHi.setter
    def ObjOstHi(self, ObjOstHi: str):
        self.__ObjOstHi = ObjOstHi

    @property
    def ObjOset(self) -> str:
        return self.__ObjOset

    @ObjOset.setter
    def ObjOset(self, ObjOset: str):
        self.__ObjOset = ObjOset

    @property
    def ObjTpe(self) -> str:
        return self.__ObjTpe

    @ObjTpe.setter
    def ObjTpe(self, ObjTpe: str):
        self.__ObjTpe = ObjTpe

class afpText_GSCS(triplet):

    def __init__(self, LCID: str):
        self.LCID = LCID
        
    @property
    def LCID(self) -> str:
        return self.__LCID

    @LCID.setter
    def LCID(self, LCID: str):
        self.__LCID = LCID

class afpText_BeginSegmentCommand(triplet):

    def __init__(self, LENGTH: str, NAME: str, FLAG1: str, FLAG2: str, SEGL: str, PSNAME: str):
        self.LENGTH = LENGTH
        self.NAME = NAME
        self.FLAG1 = FLAG1
        self.FLAG2 = FLAG2
        self.SEGL = SEGL
        self.PSNAME = PSNAME
        
    @property
    def FLAG1(self) -> str:
        return self.__FLAG1

    @FLAG1.setter
    def FLAG1(self, FLAG1: str):
        self.__FLAG1 = FLAG1

    @property
    def NAME(self) -> str:
        return self.__NAME

    @NAME.setter
    def NAME(self, NAME: str):
        self.__NAME = NAME

    @property
    def SEGL(self) -> str:
        return self.__SEGL

    @SEGL.setter
    def SEGL(self, SEGL: str):
        self.__SEGL = SEGL

    @property
    def LENGTH(self) -> str:
        return self.__LENGTH

    @LENGTH.setter
    def LENGTH(self, LENGTH: str):
        self.__LENGTH = LENGTH

    @property
    def FLAG2(self) -> str:
        return self.__FLAG2

    @FLAG2.setter
    def FLAG2(self, FLAG2: str):
        self.__FLAG2 = FLAG2

    @property
    def PSNAME(self) -> str:
        return self.__PSNAME

    @PSNAME.setter
    def PSNAME(self, PSNAME: str):
        self.__PSNAME = PSNAME

class afpText_BLN(triplet):

    pass
class afpText_PresentationSpaceResetMixing(triplet):

    def __init__(self, BgMxFlag: str):
        self.BgMxFlag = BgMxFlag
        
    @property
    def BgMxFlag(self) -> str:
        return self.__BgMxFlag

    @BgMxFlag.setter
    def BgMxFlag(self, BgMxFlag: str):
        self.__BgMxFlag = BgMxFlag

class afpText_FontDescriptorSpecification(triplet):

    def __init__(self, FtWtClass: str, FtWdClass: str, FtHeight: str, FtWidth: str, FtDsFlags: str, FtUsFlags: str):
        self.FtWtClass = FtWtClass
        self.FtWdClass = FtWdClass
        self.FtHeight = FtHeight
        self.FtWidth = FtWidth
        self.FtDsFlags = FtDsFlags
        self.FtUsFlags = FtUsFlags
        
    @property
    def FtWdClass(self) -> str:
        return self.__FtWdClass

    @FtWdClass.setter
    def FtWdClass(self, FtWdClass: str):
        self.__FtWdClass = FtWdClass

    @property
    def FtHeight(self) -> str:
        return self.__FtHeight

    @FtHeight.setter
    def FtHeight(self, FtHeight: str):
        self.__FtHeight = FtHeight

    @property
    def FtWidth(self) -> str:
        return self.__FtWidth

    @FtWidth.setter
    def FtWidth(self, FtWidth: str):
        self.__FtWidth = FtWidth

    @property
    def FtUsFlags(self) -> str:
        return self.__FtUsFlags

    @FtUsFlags.setter
    def FtUsFlags(self, FtUsFlags: str):
        self.__FtUsFlags = FtUsFlags

    @property
    def FtWtClass(self) -> str:
        return self.__FtWtClass

    @FtWtClass.setter
    def FtWtClass(self, FtWtClass: str):
        self.__FtWtClass = FtWtClass

    @property
    def FtDsFlags(self) -> str:
        return self.__FtDsFlags

    @FtDsFlags.setter
    def FtDsFlags(self, FtDsFlags: str):
        self.__FtDsFlags = FtDsFlags

class afpText_NOPCS(triplet):

    def __init__(self, IGNDATA: str):
        self.IGNDATA = IGNDATA
        
    @property
    def IGNDATA(self) -> str:
        return self.__IGNDATA

    @IGNDATA.setter
    def IGNDATA(self, IGNDATA: str):
        self.__IGNDATA = IGNDATA

class afpText_IncludeTile(triplet):

    def __init__(self, TIRID: str):
        self.TIRID = TIRID
        
    @property
    def TIRID(self) -> str:
        return self.__TIRID

    @TIRID.setter
    def TIRID(self, TIRID: str):
        self.__TIRID = TIRID

class afpText_ObjectOriginIdentifier(triplet):

    def __init__(self, System: str, SysID: str, MedID: str, DSID: str):
        self.System = System
        self.SysID = SysID
        self.MedID = MedID
        self.DSID = DSID
        
    @property
    def System(self) -> str:
        return self.__System

    @System.setter
    def System(self, System: str):
        self.__System = System

    @property
    def SysID(self) -> str:
        return self.__SysID

    @SysID.setter
    def SysID(self, SysID: str):
        self.__SysID = SysID

    @property
    def DSID(self) -> str:
        return self.__DSID

    @DSID.setter
    def DSID(self, DSID: str):
        self.__DSID = DSID

    @property
    def MedID(self) -> str:
        return self.__MedID

    @MedID.setter
    def MedID(self, MedID: str):
        self.__MedID = MedID

class afpText_BeginSegment(triplet):

    def __init__(self, SEGNAME: str):
        self.SEGNAME = SEGNAME
        
    @property
    def SEGNAME(self) -> str:
        return self.__SEGNAME

    @SEGNAME.setter
    def SEGNAME(self, SEGNAME: str):
        self.__SEGNAME = SEGNAME

class afpText_ImageResolution(triplet):

    def __init__(self, XBase: str, YBase: str, XResol: str, YResol: str):
        self.XBase = XBase
        self.YBase = YBase
        self.XResol = XResol
        self.YResol = YResol
        
    @property
    def YBase(self) -> str:
        return self.__YBase

    @YBase.setter
    def YBase(self, YBase: str):
        self.__YBase = YBase

    @property
    def XBase(self) -> str:
        return self.__XBase

    @XBase.setter
    def XBase(self, XBase: str):
        self.__XBase = XBase

    @property
    def XResol(self) -> str:
        return self.__XResol

    @XResol.setter
    def XResol(self, XResol: str):
        self.__XResol = XResol

    @property
    def YResol(self) -> str:
        return self.__YResol

    @YResol.setter
    def YResol(self, YResol: str):
        self.__YResol = YResol

class afpText_GSCP(triplet):

    def __init__(self, XPOS: str, YPOS: str):
        self.XPOS = XPOS
        self.YPOS = YPOS
        
    @property
    def YPOS(self) -> str:
        return self.__YPOS

    @YPOS.setter
    def YPOS(self, YPOS: str):
        self.__YPOS = YPOS

    @property
    def XPOS(self) -> str:
        return self.__XPOS

    @XPOS.setter
    def XPOS(self, XPOS: str):
        self.__XPOS = XPOS

class afpText_GCFARC(triplet):

    def __init__(self, MH: str, MFR: str):
        self.MH = MH
        self.MFR = MFR
        
    @property
    def MFR(self) -> str:
        return self.__MFR

    @MFR.setter
    def MFR(self, MFR: str):
        self.__MFR = MFR

    @property
    def MH(self) -> str:
        return self.__MH

    @MH.setter
    def MH(self, MH: str):
        self.__MH = MH

class afpText_EncodingSchemeID(triplet):

    def __init__(self, ESidCP: str, ESidUD: str):
        self.ESidCP = ESidCP
        self.ESidUD = ESidUD
        
    @property
    def ESidCP(self) -> str:
        return self.__ESidCP

    @ESidCP.setter
    def ESidCP(self, ESidCP: str):
        self.__ESidCP = ESidCP

    @property
    def ESidUD(self) -> str:
        return self.__ESidUD

    @ESidUD.setter
    def ESidUD(self, ESidUD: str):
        self.__ESidUD = ESidUD

class afpText_FontCodedGraphicCharacterSetGlobalIdentifier(triplet):

    def __init__(self, GCSGID: str, CPGID: str):
        self.GCSGID = GCSGID
        self.CPGID = CPGID
        
    @property
    def GCSGID(self) -> str:
        return self.__GCSGID

    @GCSGID.setter
    def GCSGID(self, GCSGID: str):
        self.__GCSGID = GCSGID

    @property
    def CPGID(self) -> str:
        return self.__CPGID

    @CPGID.setter
    def CPGID(self, CPGID: str):
        self.__CPGID = CPGID

class afpText_GCOMT(triplet):

    def __init__(self, DATA: str):
        self.DATA = DATA
        
    @property
    def DATA(self) -> str:
        return self.__DATA

    @DATA.setter
    def DATA(self, DATA: str):
        self.__DATA = DATA

class afpText_UP3iFinishingOperation(triplet):

    def __init__(self, Seqnum: str, UP3iDat: str):
        self.Seqnum = Seqnum
        self.UP3iDat = UP3iDat
        
    @property
    def UP3iDat(self) -> str:
        return self.__UP3iDat

    @UP3iDat.setter
    def UP3iDat(self, UP3iDat: str):
        self.__UP3iDat = UP3iDat

    @property
    def Seqnum(self) -> str:
        return self.__Seqnum

    @Seqnum.setter
    def Seqnum(self, Seqnum: str):
        self.__Seqnum = Seqnum

class afpText_ObjectContainerPresentationSpaceSize(triplet):

    def __init__(self, PDFSize: str):
        self.PDFSize = PDFSize
        
    @property
    def PDFSize(self) -> str:
        return self.__PDFSize

    @PDFSize.setter
    def PDFSize(self, PDFSize: str):
        self.__PDFSize = PDFSize

class afpText_SetBiLevelImageColor(triplet):

    def __init__(self, AREA: str, Reserved: str, NAMECOLR: str):
        self.AREA = AREA
        self.Reserved = Reserved
        self.NAMECOLR = NAMECOLR
        
    @property
    def AREA(self) -> str:
        return self.__AREA

    @AREA.setter
    def AREA(self, AREA: str):
        self.__AREA = AREA

    @property
    def Reserved(self) -> str:
        return self.__Reserved

    @Reserved.setter
    def Reserved(self, Reserved: str):
        self.__Reserved = Reserved

    @property
    def NAMECOLR(self) -> str:
        return self.__NAMECOLR

    @NAMECOLR.setter
    def NAMECOLR(self, NAMECOLR: str):
        self.__NAMECOLR = NAMECOLR

class afpText_ObjectStructuredFieldOffset(triplet):

    def __init__(self, SFOff: str, SFOffHi: str):
        self.SFOff = SFOff
        self.SFOffHi = SFOffHi
        
    @property
    def SFOffHi(self) -> str:
        return self.__SFOffHi

    @SFOffHi.setter
    def SFOffHi(self, SFOffHi: str):
        self.__SFOffHi = SFOffHi

    @property
    def SFOff(self) -> str:
        return self.__SFOff

    @SFOff.setter
    def SFOff(self, SFOff: str):
        self.__SFOff = SFOff

class afpText_CharacterRotation(triplet):

    def __init__(self, CharRot: str):
        self.CharRot = CharRot
        
    @property
    def CharRot(self) -> str:
        return self.__CharRot

    @CharRot.setter
    def CharRot(self, CharRot: str):
        self.__CharRot = CharRot

class afpText_ResourceLocalIdentifier(triplet):

    def __init__(self, ResType: str, ResLID: str):
        self.ResType = ResType
        self.ResLID = ResLID
        
    @property
    def ResType(self) -> str:
        return self.__ResType

    @ResType.setter
    def ResType(self, ResType: str):
        self.__ResType = ResType

    @property
    def ResLID(self) -> str:
        return self.__ResLID

    @ResLID.setter
    def ResLID(self, ResLID: str):
        self.__ResLID = ResLID

class afpText_ObjectByteOffset(triplet):

    def __init__(self, DirByOff: str, DirByHi: str):
        self.DirByOff = DirByOff
        self.DirByHi = DirByHi
        
    @property
    def DirByHi(self) -> str:
        return self.__DirByHi

    @DirByHi.setter
    def DirByHi(self, DirByHi: str):
        self.__DirByHi = DirByHi

    @property
    def DirByOff(self) -> str:
        return self.__DirByOff

    @DirByOff.setter
    def DirByOff(self, DirByOff: str):
        self.__DirByOff = DirByOff

class afpText_GCBIMG(triplet):

    def __init__(self, FORMAT: str, RES: str, WIDTH: str, HEIGHT: str):
        self.FORMAT = FORMAT
        self.RES = RES
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        
    @property
    def WIDTH(self) -> str:
        return self.__WIDTH

    @WIDTH.setter
    def WIDTH(self, WIDTH: str):
        self.__WIDTH = WIDTH

    @property
    def RES(self) -> str:
        return self.__RES

    @RES.setter
    def RES(self, RES: str):
        self.__RES = RES

    @property
    def FORMAT(self) -> str:
        return self.__FORMAT

    @FORMAT.setter
    def FORMAT(self, FORMAT: str):
        self.__FORMAT = FORMAT

    @property
    def HEIGHT(self) -> str:
        return self.__HEIGHT

    @HEIGHT.setter
    def HEIGHT(self, HEIGHT: str):
        self.__HEIGHT = HEIGHT

class afpText_ColorFidelity(triplet):

    def __init__(self, StpCoEx: str, RepCoEx: str, ColSub: str):
        self.StpCoEx = StpCoEx
        self.RepCoEx = RepCoEx
        self.ColSub = ColSub
        
    @property
    def StpCoEx(self) -> str:
        return self.__StpCoEx

    @StpCoEx.setter
    def StpCoEx(self, StpCoEx: str):
        self.__StpCoEx = StpCoEx

    @property
    def RepCoEx(self) -> str:
        return self.__RepCoEx

    @RepCoEx.setter
    def RepCoEx(self, RepCoEx: str):
        self.__RepCoEx = RepCoEx

    @property
    def ColSub(self) -> str:
        return self.__ColSub

    @ColSub.setter
    def ColSub(self, ColSub: str):
        self.__ColSub = ColSub

class afpText_GBOX(triplet):

    def __init__(self, RES: str, XPOS0: str, YPOS0: str, XPOS1: str, YPOS1: str, HAXIS: str, VAXIS: str):
        self.RES = RES
        self.XPOS0 = XPOS0
        self.YPOS0 = YPOS0
        self.XPOS1 = XPOS1
        self.YPOS1 = YPOS1
        self.HAXIS = HAXIS
        self.VAXIS = VAXIS
        
    @property
    def RES(self) -> str:
        return self.__RES

    @RES.setter
    def RES(self, RES: str):
        self.__RES = RES

    @property
    def XPOS1(self) -> str:
        return self.__XPOS1

    @XPOS1.setter
    def XPOS1(self, XPOS1: str):
        self.__XPOS1 = XPOS1

    @property
    def YPOS0(self) -> str:
        return self.__YPOS0

    @YPOS0.setter
    def YPOS0(self, YPOS0: str):
        self.__YPOS0 = YPOS0

    @property
    def VAXIS(self) -> str:
        return self.__VAXIS

    @VAXIS.setter
    def VAXIS(self, VAXIS: str):
        self.__VAXIS = VAXIS

    @property
    def YPOS1(self) -> str:
        return self.__YPOS1

    @YPOS1.setter
    def YPOS1(self, YPOS1: str):
        self.__YPOS1 = YPOS1

    @property
    def HAXIS(self) -> str:
        return self.__HAXIS

    @HAXIS.setter
    def HAXIS(self, HAXIS: str):
        self.__HAXIS = HAXIS

    @property
    def XPOS0(self) -> str:
        return self.__XPOS0

    @XPOS0.setter
    def XPOS0(self, XPOS0: str):
        self.__XPOS0 = XPOS0

class afpText_CMRFidelity(triplet):

    def __init__(self, StpCMREx: str, RepCMREx: str):
        self.StpCMREx = StpCMREx
        self.RepCMREx = RepCMREx
        
    @property
    def StpCMREx(self) -> str:
        return self.__StpCMREx

    @StpCMREx.setter
    def StpCMREx(self, StpCMREx: str):
        self.__StpCMREx = StpCMREx

    @property
    def RepCMREx(self) -> str:
        return self.__RepCMREx

    @RepCMREx.setter
    def RepCMREx(self, RepCMREx: str):
        self.__RepCMREx = RepCMREx

class afpText_GCCBEZ(triplet):

    pass
class afpText_AMB(triplet):

    def __init__(self, DSPLCMNT: str):
        self.DSPLCMNT = DSPLCMNT
        
    @property
    def DSPLCMNT(self) -> str:
        return self.__DSPLCMNT

    @DSPLCMNT.setter
    def DSPLCMNT(self, DSPLCMNT: str):
        self.__DSPLCMNT = DSPLCMNT

class afpText_GCCBEZRG:

    def __init__(self, XPOS: str, YPOS: str, afpText_GCCBEZRG: "afpText_GCCBEZ" = None):
        self.XPOS = XPOS
        self.YPOS = YPOS
        self.afpText_GCCBEZRG = afpText_GCCBEZRG
        
    @property
    def YPOS(self) -> str:
        return self.__YPOS

    @YPOS.setter
    def YPOS(self, YPOS: str):
        self.__YPOS = YPOS

    @property
    def XPOS(self) -> str:
        return self.__XPOS

    @XPOS.setter
    def XPOS(self, XPOS: str):
        self.__XPOS = XPOS

    @property
    def afpText_GCCBEZRG(self):
        return self.__afpText_GCCBEZRG

    @afpText_GCCBEZRG.setter
    def afpText_GCCBEZRG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_GCCBEZRG__afpText_GCCBEZRG", None)
        self.__afpText_GCCBEZRG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_GCCBEZ"):
                opp_val = getattr(old_value, "afpText_GCCBEZ", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_GCCBEZ"):
                opp_val = getattr(value, "afpText_GCCBEZ", None)
                if opp_val is None:
                    setattr(value, "afpText_GCCBEZ", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_GCBEZRG:

    def __init__(self, XPOS: str, YPOS: str, afpText_GCBEZRG: "afpText_GCBEZ" = None):
        self.XPOS = XPOS
        self.YPOS = YPOS
        self.afpText_GCBEZRG = afpText_GCBEZRG
        
    @property
    def YPOS(self) -> str:
        return self.__YPOS

    @YPOS.setter
    def YPOS(self, YPOS: str):
        self.__YPOS = YPOS

    @property
    def XPOS(self) -> str:
        return self.__XPOS

    @XPOS.setter
    def XPOS(self, XPOS: str):
        self.__XPOS = XPOS

    @property
    def afpText_GCBEZRG(self):
        return self.__afpText_GCBEZRG

    @afpText_GCBEZRG.setter
    def afpText_GCBEZRG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_GCBEZRG__afpText_GCBEZRG", None)
        self.__afpText_GCBEZRG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_GCBEZ"):
                opp_val = getattr(old_value, "afpText_GCBEZ", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_GCBEZ"):
                opp_val = getattr(value, "afpText_GCBEZ", None)
                if opp_val is None:
                    setattr(value, "afpText_GCBEZ", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_FNNRG:

    def __init__(self, GCGID: str, TSOffset: str):
        self.GCGID = GCGID
        self.TSOffset = TSOffset
        
    @property
    def TSOffset(self) -> str:
        return self.__TSOffset

    @TSOffset.setter
    def TSOffset(self, TSOffset: str):
        self.__TSOffset = TSOffset

    @property
    def GCGID(self) -> str:
        return self.__GCGID

    @GCGID.setter
    def GCGID(self, GCGID: str):
        self.__GCGID = GCGID

class afpText_ExternalAlgorithmRG:

    def __init__(self, DIRCTN: str, PADBDRY: str, PADALMT: str, afpText_ExternalAlgorithmRG: "afpText_ExternalAlgorithm" = None):
        self.DIRCTN = DIRCTN
        self.PADBDRY = PADBDRY
        self.PADALMT = PADALMT
        self.afpText_ExternalAlgorithmRG = afpText_ExternalAlgorithmRG
        
    @property
    def DIRCTN(self) -> str:
        return self.__DIRCTN

    @DIRCTN.setter
    def DIRCTN(self, DIRCTN: str):
        self.__DIRCTN = DIRCTN

    @property
    def PADALMT(self) -> str:
        return self.__PADALMT

    @PADALMT.setter
    def PADALMT(self, PADALMT: str):
        self.__PADALMT = PADALMT

    @property
    def PADBDRY(self) -> str:
        return self.__PADBDRY

    @PADBDRY.setter
    def PADBDRY(self, PADBDRY: str):
        self.__PADBDRY = PADBDRY

    @property
    def afpText_ExternalAlgorithmRG(self):
        return self.__afpText_ExternalAlgorithmRG

    @afpText_ExternalAlgorithmRG.setter
    def afpText_ExternalAlgorithmRG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_ExternalAlgorithmRG__afpText_ExternalAlgorithmRG", None)
        self.__afpText_ExternalAlgorithmRG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_ExternalAlgorithm"):
                opp_val = getattr(old_value, "afpText_ExternalAlgorithm", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_ExternalAlgorithm"):
                opp_val = getattr(value, "afpText_ExternalAlgorithm", None)
                if opp_val is None:
                    setattr(value, "afpText_ExternalAlgorithm", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_GCLINERG:

    def __init__(self, XPOS: str, YPOS: str, afpText_GCLINERG: "afpText_GCLINE" = None):
        self.XPOS = XPOS
        self.YPOS = YPOS
        self.afpText_GCLINERG = afpText_GCLINERG
        
    @property
    def YPOS(self) -> str:
        return self.__YPOS

    @YPOS.setter
    def YPOS(self, YPOS: str):
        self.__YPOS = YPOS

    @property
    def XPOS(self) -> str:
        return self.__XPOS

    @XPOS.setter
    def XPOS(self, XPOS: str):
        self.__XPOS = XPOS

    @property
    def afpText_GCLINERG(self):
        return self.__afpText_GCLINERG

    @afpText_GCLINERG.setter
    def afpText_GCLINERG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_GCLINERG__afpText_GCLINERG", None)
        self.__afpText_GCLINERG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_GCLINE"):
                opp_val = getattr(old_value, "afpText_GCLINE", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_GCLINE"):
                opp_val = getattr(value, "afpText_GCLINE", None)
                if opp_val is None:
                    setattr(value, "afpText_GCLINE", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_GLINERG:

    def __init__(self, XPOS: str, YPOS: str, afpText_GLINERG: "afpText_GLINE" = None):
        self.XPOS = XPOS
        self.YPOS = YPOS
        self.afpText_GLINERG = afpText_GLINERG
        
    @property
    def XPOS(self) -> str:
        return self.__XPOS

    @XPOS.setter
    def XPOS(self, XPOS: str):
        self.__XPOS = XPOS

    @property
    def YPOS(self) -> str:
        return self.__YPOS

    @YPOS.setter
    def YPOS(self, YPOS: str):
        self.__YPOS = YPOS

    @property
    def afpText_GLINERG(self):
        return self.__afpText_GLINERG

    @afpText_GLINERG.setter
    def afpText_GLINERG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_GLINERG__afpText_GLINERG", None)
        self.__afpText_GLINERG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_GLINE"):
                opp_val = getattr(old_value, "afpText_GLINE", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_GLINE"):
                opp_val = getattr(value, "afpText_GLINE", None)
                if opp_val is None:
                    setattr(value, "afpText_GLINE", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_GCFLTRG:

    def __init__(self, XPOS: str, YPOS: str, afpText_GCFLTRG: "afpText_GCFLT" = None):
        self.XPOS = XPOS
        self.YPOS = YPOS
        self.afpText_GCFLTRG = afpText_GCFLTRG
        
    @property
    def XPOS(self) -> str:
        return self.__XPOS

    @XPOS.setter
    def XPOS(self, XPOS: str):
        self.__XPOS = XPOS

    @property
    def YPOS(self) -> str:
        return self.__YPOS

    @YPOS.setter
    def YPOS(self, YPOS: str):
        self.__YPOS = YPOS

    @property
    def afpText_GCFLTRG(self):
        return self.__afpText_GCFLTRG

    @afpText_GCFLTRG.setter
    def afpText_GCFLTRG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_GCFLTRG__afpText_GCFLTRG", None)
        self.__afpText_GCFLTRG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_GCFLT"):
                opp_val = getattr(old_value, "afpText_GCFLT", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_GCFLT"):
                opp_val = getattr(value, "afpText_GCFLT", None)
                if opp_val is None:
                    setattr(value, "afpText_GCFLT", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_GFLTRG:

    def __init__(self, XPOS: str, YPOS: str, afpText_GFLTRG: "afpText_GFLT" = None):
        self.XPOS = XPOS
        self.YPOS = YPOS
        self.afpText_GFLTRG = afpText_GFLTRG
        
    @property
    def XPOS(self) -> str:
        return self.__XPOS

    @XPOS.setter
    def XPOS(self, XPOS: str):
        self.__XPOS = XPOS

    @property
    def YPOS(self) -> str:
        return self.__YPOS

    @YPOS.setter
    def YPOS(self, YPOS: str):
        self.__YPOS = YPOS

    @property
    def afpText_GFLTRG(self):
        return self.__afpText_GFLTRG

    @afpText_GFLTRG.setter
    def afpText_GFLTRG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_GFLTRG__afpText_GFLTRG", None)
        self.__afpText_GFLTRG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_GFLT"):
                opp_val = getattr(old_value, "afpText_GFLT", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_GFLT"):
                opp_val = getattr(value, "afpText_GFLT", None)
                if opp_val is None:
                    setattr(value, "afpText_GFLT", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_SamplingRatiosRG:

    def __init__(self, HSAMPLE: str, VSAMPLE: str, afpText_SamplingRatiosRG: "afpText_SamplingRatios" = None):
        self.HSAMPLE = HSAMPLE
        self.VSAMPLE = VSAMPLE
        self.afpText_SamplingRatiosRG = afpText_SamplingRatiosRG
        
    @property
    def HSAMPLE(self) -> str:
        return self.__HSAMPLE

    @HSAMPLE.setter
    def HSAMPLE(self, HSAMPLE: str):
        self.__HSAMPLE = HSAMPLE

    @property
    def VSAMPLE(self) -> str:
        return self.__VSAMPLE

    @VSAMPLE.setter
    def VSAMPLE(self, VSAMPLE: str):
        self.__VSAMPLE = VSAMPLE

    @property
    def afpText_SamplingRatiosRG(self):
        return self.__afpText_SamplingRatiosRG

    @afpText_SamplingRatiosRG.setter
    def afpText_SamplingRatiosRG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_SamplingRatiosRG__afpText_SamplingRatiosRG", None)
        self.__afpText_SamplingRatiosRG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_SamplingRatios"):
                opp_val = getattr(old_value, "afpText_SamplingRatios", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_SamplingRatios"):
                opp_val = getattr(value, "afpText_SamplingRatios", None)
                if opp_val is None:
                    setattr(value, "afpText_SamplingRatios", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_TileTOCRG:

    def __init__(self, XOFFSET: str, YOFFSET: str, THSIZE: str, TVSIZE: str, RELRES: str, COMPR: str, DATAPOS: str, afpText_TileTOCRG: "afpText_TileTOC" = None):
        self.XOFFSET = XOFFSET
        self.YOFFSET = YOFFSET
        self.THSIZE = THSIZE
        self.TVSIZE = TVSIZE
        self.RELRES = RELRES
        self.COMPR = COMPR
        self.DATAPOS = DATAPOS
        self.afpText_TileTOCRG = afpText_TileTOCRG
        
    @property
    def DATAPOS(self) -> str:
        return self.__DATAPOS

    @DATAPOS.setter
    def DATAPOS(self, DATAPOS: str):
        self.__DATAPOS = DATAPOS

    @property
    def COMPR(self) -> str:
        return self.__COMPR

    @COMPR.setter
    def COMPR(self, COMPR: str):
        self.__COMPR = COMPR

    @property
    def XOFFSET(self) -> str:
        return self.__XOFFSET

    @XOFFSET.setter
    def XOFFSET(self, XOFFSET: str):
        self.__XOFFSET = XOFFSET

    @property
    def YOFFSET(self) -> str:
        return self.__YOFFSET

    @YOFFSET.setter
    def YOFFSET(self, YOFFSET: str):
        self.__YOFFSET = YOFFSET

    @property
    def TVSIZE(self) -> str:
        return self.__TVSIZE

    @TVSIZE.setter
    def TVSIZE(self, TVSIZE: str):
        self.__TVSIZE = TVSIZE

    @property
    def THSIZE(self) -> str:
        return self.__THSIZE

    @THSIZE.setter
    def THSIZE(self, THSIZE: str):
        self.__THSIZE = THSIZE

    @property
    def RELRES(self) -> str:
        return self.__RELRES

    @RELRES.setter
    def RELRES(self, RELRES: str):
        self.__RELRES = RELRES

    @property
    def afpText_TileTOCRG(self):
        return self.__afpText_TileTOCRG

    @afpText_TileTOCRG.setter
    def afpText_TileTOCRG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_TileTOCRG__afpText_TileTOCRG", None)
        self.__afpText_TileTOCRG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_TileTOC"):
                opp_val = getattr(old_value, "afpText_TileTOC", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_TileTOC"):
                opp_val = getattr(value, "afpText_TileTOC", None)
                if opp_val is None:
                    setattr(value, "afpText_TileTOC", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_BandImageRG:

    def __init__(self, BITCNT: str, afpText_BandImageRG: "afpText_BandImage" = None):
        self.BITCNT = BITCNT
        self.afpText_BandImageRG = afpText_BandImageRG
        
    @property
    def BITCNT(self) -> str:
        return self.__BITCNT

    @BITCNT.setter
    def BITCNT(self, BITCNT: str):
        self.__BITCNT = BITCNT

    @property
    def afpText_BandImageRG(self):
        return self.__afpText_BandImageRG

    @afpText_BandImageRG.setter
    def afpText_BandImageRG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_BandImageRG__afpText_BandImageRG", None)
        self.__afpText_BandImageRG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_BandImage"):
                opp_val = getattr(old_value, "afpText_BandImage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_BandImage"):
                opp_val = getattr(value, "afpText_BandImage", None)
                if opp_val is None:
                    setattr(value, "afpText_BandImage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_PPORG:

    def __init__(self, RGLength: str, ObjType: str, ProcFlgs: str, XocaOset: str, YocaOset: str, afpText_PPORG: "afpText_PPO" = None, afpText_PPORG185: set["afpText_triplet"] = None):
        self.RGLength = RGLength
        self.ObjType = ObjType
        self.ProcFlgs = ProcFlgs
        self.XocaOset = XocaOset
        self.YocaOset = YocaOset
        self.afpText_PPORG = afpText_PPORG
        self.afpText_PPORG185 = afpText_PPORG185 if afpText_PPORG185 is not None else set()
        
    @property
    def ObjType(self) -> str:
        return self.__ObjType

    @ObjType.setter
    def ObjType(self, ObjType: str):
        self.__ObjType = ObjType

    @property
    def XocaOset(self) -> str:
        return self.__XocaOset

    @XocaOset.setter
    def XocaOset(self, XocaOset: str):
        self.__XocaOset = XocaOset

    @property
    def YocaOset(self) -> str:
        return self.__YocaOset

    @YocaOset.setter
    def YocaOset(self, YocaOset: str):
        self.__YocaOset = YocaOset

    @property
    def RGLength(self) -> str:
        return self.__RGLength

    @RGLength.setter
    def RGLength(self, RGLength: str):
        self.__RGLength = RGLength

    @property
    def ProcFlgs(self) -> str:
        return self.__ProcFlgs

    @ProcFlgs.setter
    def ProcFlgs(self, ProcFlgs: str):
        self.__ProcFlgs = ProcFlgs

    @property
    def afpText_PPORG(self):
        return self.__afpText_PPORG

    @afpText_PPORG.setter
    def afpText_PPORG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_PPORG__afpText_PPORG", None)
        self.__afpText_PPORG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_PPO"):
                opp_val = getattr(old_value, "afpText_PPO", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_PPO"):
                opp_val = getattr(value, "afpText_PPO", None)
                if opp_val is None:
                    setattr(value, "afpText_PPO", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def afpText_PPORG185(self):
        return self.__afpText_PPORG185

    @afpText_PPORG185.setter
    def afpText_PPORG185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_PPORG__afpText_PPORG185", None)
        self.__afpText_PPORG185 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet186"):
                    opp_val = getattr(item, "afpText_triplet186", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet186", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet186"):
                    opp_val = getattr(item, "afpText_triplet186", None)
                    
                    setattr(item, "afpText_triplet186", self)
                    

class afpText_PGPRG:

    def __init__(self, RGLength: str, XmOset: str, YmOset: str, PGorient: str, SHside: str, PgFlgs: str, PMCid: str, afpText_PGPRG: "afpText_PGP" = None):
        self.RGLength = RGLength
        self.XmOset = XmOset
        self.YmOset = YmOset
        self.PGorient = PGorient
        self.SHside = SHside
        self.PgFlgs = PgFlgs
        self.PMCid = PMCid
        self.afpText_PGPRG = afpText_PGPRG
        
    @property
    def YmOset(self) -> str:
        return self.__YmOset

    @YmOset.setter
    def YmOset(self, YmOset: str):
        self.__YmOset = YmOset

    @property
    def PGorient(self) -> str:
        return self.__PGorient

    @PGorient.setter
    def PGorient(self, PGorient: str):
        self.__PGorient = PGorient

    @property
    def SHside(self) -> str:
        return self.__SHside

    @SHside.setter
    def SHside(self, SHside: str):
        self.__SHside = SHside

    @property
    def PgFlgs(self) -> str:
        return self.__PgFlgs

    @PgFlgs.setter
    def PgFlgs(self, PgFlgs: str):
        self.__PgFlgs = PgFlgs

    @property
    def PMCid(self) -> str:
        return self.__PMCid

    @PMCid.setter
    def PMCid(self, PMCid: str):
        self.__PMCid = PMCid

    @property
    def RGLength(self) -> str:
        return self.__RGLength

    @RGLength.setter
    def RGLength(self, RGLength: str):
        self.__RGLength = RGLength

    @property
    def XmOset(self) -> str:
        return self.__XmOset

    @XmOset.setter
    def XmOset(self, XmOset: str):
        self.__XmOset = XmOset

    @property
    def afpText_PGPRG(self):
        return self.__afpText_PGPRG

    @afpText_PGPRG.setter
    def afpText_PGPRG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_PGPRG__afpText_PGPRG", None)
        self.__afpText_PGPRG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_PGP"):
                opp_val = getattr(old_value, "afpText_PGP", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_PGP"):
                opp_val = getattr(value, "afpText_PGP", None)
                if opp_val is None:
                    setattr(value, "afpText_PGP", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_MPSRG:

    def __init__(self, Reserved: str, PsegName: str, afpText_MPSRG: "afpText_MPS" = None):
        self.Reserved = Reserved
        self.PsegName = PsegName
        self.afpText_MPSRG = afpText_MPSRG
        
    @property
    def PsegName(self) -> str:
        return self.__PsegName

    @PsegName.setter
    def PsegName(self, PsegName: str):
        self.__PsegName = PsegName

    @property
    def Reserved(self) -> str:
        return self.__Reserved

    @Reserved.setter
    def Reserved(self, Reserved: str):
        self.__Reserved = Reserved

    @property
    def afpText_MPSRG(self):
        return self.__afpText_MPSRG

    @afpText_MPSRG.setter
    def afpText_MPSRG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MPSRG__afpText_MPSRG", None)
        self.__afpText_MPSRG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_MPS"):
                opp_val = getattr(old_value, "afpText_MPS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_MPS"):
                opp_val = getattr(value, "afpText_MPS", None)
                if opp_val is None:
                    setattr(value, "afpText_MPS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_MPORG:

    def __init__(self, RGLength: str, afpText_MPORG: "afpText_MPO" = None, afpText_MPORG182: set["afpText_triplet"] = None):
        self.RGLength = RGLength
        self.afpText_MPORG = afpText_MPORG
        self.afpText_MPORG182 = afpText_MPORG182 if afpText_MPORG182 is not None else set()
        
    @property
    def RGLength(self) -> str:
        return self.__RGLength

    @RGLength.setter
    def RGLength(self, RGLength: str):
        self.__RGLength = RGLength

    @property
    def afpText_MPORG(self):
        return self.__afpText_MPORG

    @afpText_MPORG.setter
    def afpText_MPORG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MPORG__afpText_MPORG", None)
        self.__afpText_MPORG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_MPO"):
                opp_val = getattr(old_value, "afpText_MPO", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_MPO"):
                opp_val = getattr(value, "afpText_MPO", None)
                if opp_val is None:
                    setattr(value, "afpText_MPO", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def afpText_MPORG182(self):
        return self.__afpText_MPORG182

    @afpText_MPORG182.setter
    def afpText_MPORG182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MPORG__afpText_MPORG182", None)
        self.__afpText_MPORG182 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet183"):
                    opp_val = getattr(item, "afpText_triplet183", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet183", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet183"):
                    opp_val = getattr(item, "afpText_triplet183", None)
                    
                    setattr(item, "afpText_triplet183", self)
                    

class afpText_MPGRG:

    def __init__(self, RGLength: str, afpText_MPGRG: "afpText_MPG" = None, afpText_MPGRG179: set["afpText_triplet"] = None):
        self.RGLength = RGLength
        self.afpText_MPGRG = afpText_MPGRG
        self.afpText_MPGRG179 = afpText_MPGRG179 if afpText_MPGRG179 is not None else set()
        
    @property
    def RGLength(self) -> str:
        return self.__RGLength

    @RGLength.setter
    def RGLength(self, RGLength: str):
        self.__RGLength = RGLength

    @property
    def afpText_MPGRG179(self):
        return self.__afpText_MPGRG179

    @afpText_MPGRG179.setter
    def afpText_MPGRG179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MPGRG__afpText_MPGRG179", None)
        self.__afpText_MPGRG179 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet180"):
                    opp_val = getattr(item, "afpText_triplet180", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet180", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet180"):
                    opp_val = getattr(item, "afpText_triplet180", None)
                    
                    setattr(item, "afpText_triplet180", self)
                    

    @property
    def afpText_MPGRG(self):
        return self.__afpText_MPGRG

    @afpText_MPGRG.setter
    def afpText_MPGRG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MPGRG__afpText_MPGRG", None)
        self.__afpText_MPGRG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_MPG"):
                opp_val = getattr(old_value, "afpText_MPG", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_MPG"):
                opp_val = getattr(value, "afpText_MPG", None)
                if opp_val is None:
                    setattr(value, "afpText_MPG", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_MMTRG:

    def __init__(self, RGLength: str, afpText_MMTRG: "afpText_MMT" = None, afpText_MMTRG176: set["afpText_triplet"] = None):
        self.RGLength = RGLength
        self.afpText_MMTRG = afpText_MMTRG
        self.afpText_MMTRG176 = afpText_MMTRG176 if afpText_MMTRG176 is not None else set()
        
    @property
    def RGLength(self) -> str:
        return self.__RGLength

    @RGLength.setter
    def RGLength(self, RGLength: str):
        self.__RGLength = RGLength

    @property
    def afpText_MMTRG176(self):
        return self.__afpText_MMTRG176

    @afpText_MMTRG176.setter
    def afpText_MMTRG176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MMTRG__afpText_MMTRG176", None)
        self.__afpText_MMTRG176 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet177"):
                    opp_val = getattr(item, "afpText_triplet177", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet177", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet177"):
                    opp_val = getattr(item, "afpText_triplet177", None)
                    
                    setattr(item, "afpText_triplet177", self)
                    

    @property
    def afpText_MMTRG(self):
        return self.__afpText_MMTRG

    @afpText_MMTRG.setter
    def afpText_MMTRG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MMTRG__afpText_MMTRG", None)
        self.__afpText_MMTRG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_MMT"):
                opp_val = getattr(old_value, "afpText_MMT", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_MMT"):
                opp_val = getattr(value, "afpText_MMT", None)
                if opp_val is None:
                    setattr(value, "afpText_MMT", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_MMORG:

    def __init__(self, OVLid: str, Flags: str, OVLname: str, afpText_MMORG: "afpText_MMO" = None):
        self.OVLid = OVLid
        self.Flags = Flags
        self.OVLname = OVLname
        self.afpText_MMORG = afpText_MMORG
        
    @property
    def OVLid(self) -> str:
        return self.__OVLid

    @OVLid.setter
    def OVLid(self, OVLid: str):
        self.__OVLid = OVLid

    @property
    def OVLname(self) -> str:
        return self.__OVLname

    @OVLname.setter
    def OVLname(self, OVLname: str):
        self.__OVLname = OVLname

    @property
    def Flags(self) -> str:
        return self.__Flags

    @Flags.setter
    def Flags(self, Flags: str):
        self.__Flags = Flags

    @property
    def afpText_MMORG(self):
        return self.__afpText_MMORG

    @afpText_MMORG.setter
    def afpText_MMORG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MMORG__afpText_MMORG", None)
        self.__afpText_MMORG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_MMO"):
                opp_val = getattr(old_value, "afpText_MMO", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_MMO"):
                opp_val = getattr(value, "afpText_MMO", None)
                if opp_val is None:
                    setattr(value, "afpText_MMO", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_MSURG:

    def __init__(self, SUPname: str, Reserved: str, SUPid: str, afpText_MSURG: "afpText_MSU" = None):
        self.SUPname = SUPname
        self.Reserved = Reserved
        self.SUPid = SUPid
        self.afpText_MSURG = afpText_MSURG
        
    @property
    def SUPid(self) -> str:
        return self.__SUPid

    @SUPid.setter
    def SUPid(self, SUPid: str):
        self.__SUPid = SUPid

    @property
    def Reserved(self) -> str:
        return self.__Reserved

    @Reserved.setter
    def Reserved(self, Reserved: str):
        self.__Reserved = Reserved

    @property
    def SUPname(self) -> str:
        return self.__SUPname

    @SUPname.setter
    def SUPname(self, SUPname: str):
        self.__SUPname = SUPname

    @property
    def afpText_MSURG(self):
        return self.__afpText_MSURG

    @afpText_MSURG.setter
    def afpText_MSURG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MSURG__afpText_MSURG", None)
        self.__afpText_MSURG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_MSU"):
                opp_val = getattr(old_value, "afpText_MSU", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_MSU"):
                opp_val = getattr(value, "afpText_MSU", None)
                if opp_val is None:
                    setattr(value, "afpText_MSU", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_MIORG:

    def __init__(self, RGLength: str, afpText_MIORG: "afpText_MIO" = None, afpText_MIORG170: set["afpText_triplet"] = None):
        self.RGLength = RGLength
        self.afpText_MIORG = afpText_MIORG
        self.afpText_MIORG170 = afpText_MIORG170 if afpText_MIORG170 is not None else set()
        
    @property
    def RGLength(self) -> str:
        return self.__RGLength

    @RGLength.setter
    def RGLength(self, RGLength: str):
        self.__RGLength = RGLength

    @property
    def afpText_MIORG170(self):
        return self.__afpText_MIORG170

    @afpText_MIORG170.setter
    def afpText_MIORG170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MIORG__afpText_MIORG170", None)
        self.__afpText_MIORG170 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet171"):
                    opp_val = getattr(item, "afpText_triplet171", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet171", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet171"):
                    opp_val = getattr(item, "afpText_triplet171", None)
                    
                    setattr(item, "afpText_triplet171", self)
                    

    @property
    def afpText_MIORG(self):
        return self.__afpText_MIORG

    @afpText_MIORG.setter
    def afpText_MIORG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MIORG__afpText_MIORG", None)
        self.__afpText_MIORG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_MIO"):
                opp_val = getattr(old_value, "afpText_MIO", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_MIO"):
                opp_val = getattr(value, "afpText_MIO", None)
                if opp_val is None:
                    setattr(value, "afpText_MIO", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_MGORG:

    def __init__(self, RGLength: str, afpText_MGORG: "afpText_MGO" = None, afpText_MGORG167: set["afpText_triplet"] = None):
        self.RGLength = RGLength
        self.afpText_MGORG = afpText_MGORG
        self.afpText_MGORG167 = afpText_MGORG167 if afpText_MGORG167 is not None else set()
        
    @property
    def RGLength(self) -> str:
        return self.__RGLength

    @RGLength.setter
    def RGLength(self, RGLength: str):
        self.__RGLength = RGLength

    @property
    def afpText_MGORG167(self):
        return self.__afpText_MGORG167

    @afpText_MGORG167.setter
    def afpText_MGORG167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MGORG__afpText_MGORG167", None)
        self.__afpText_MGORG167 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet168"):
                    opp_val = getattr(item, "afpText_triplet168", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet168", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet168"):
                    opp_val = getattr(item, "afpText_triplet168", None)
                    
                    setattr(item, "afpText_triplet168", self)
                    

    @property
    def afpText_MGORG(self):
        return self.__afpText_MGORG

    @afpText_MGORG.setter
    def afpText_MGORG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MGORG__afpText_MGORG", None)
        self.__afpText_MGORG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_MGO"):
                opp_val = getattr(old_value, "afpText_MGO", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_MGO"):
                opp_val = getattr(value, "afpText_MGO", None)
                if opp_val is None:
                    setattr(value, "afpText_MGO", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_MDRRG:

    def __init__(self, RGLength: str, afpText_MDRRG: "afpText_MDR" = None, afpText_MDRRG164: set["afpText_triplet"] = None):
        self.RGLength = RGLength
        self.afpText_MDRRG = afpText_MDRRG
        self.afpText_MDRRG164 = afpText_MDRRG164 if afpText_MDRRG164 is not None else set()
        
    @property
    def RGLength(self) -> str:
        return self.__RGLength

    @RGLength.setter
    def RGLength(self, RGLength: str):
        self.__RGLength = RGLength

    @property
    def afpText_MDRRG(self):
        return self.__afpText_MDRRG

    @afpText_MDRRG.setter
    def afpText_MDRRG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MDRRG__afpText_MDRRG", None)
        self.__afpText_MDRRG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_MDR"):
                opp_val = getattr(old_value, "afpText_MDR", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_MDR"):
                opp_val = getattr(value, "afpText_MDR", None)
                if opp_val is None:
                    setattr(value, "afpText_MDR", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def afpText_MDRRG164(self):
        return self.__afpText_MDRRG164

    @afpText_MDRRG164.setter
    def afpText_MDRRG164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MDRRG__afpText_MDRRG164", None)
        self.__afpText_MDRRG164 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet165"):
                    opp_val = getattr(item, "afpText_triplet165", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet165", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet165"):
                    opp_val = getattr(item, "afpText_triplet165", None)
                    
                    setattr(item, "afpText_triplet165", self)
                    

class afpText_MMDRG:

    def __init__(self, RGLength: str, afpText_MMDRG: "afpText_MMD" = None, afpText_MMDRG173: set["afpText_triplet"] = None):
        self.RGLength = RGLength
        self.afpText_MMDRG = afpText_MMDRG
        self.afpText_MMDRG173 = afpText_MMDRG173 if afpText_MMDRG173 is not None else set()
        
    @property
    def RGLength(self) -> str:
        return self.__RGLength

    @RGLength.setter
    def RGLength(self, RGLength: str):
        self.__RGLength = RGLength

    @property
    def afpText_MMDRG173(self):
        return self.__afpText_MMDRG173

    @afpText_MMDRG173.setter
    def afpText_MMDRG173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MMDRG__afpText_MMDRG173", None)
        self.__afpText_MMDRG173 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet174"):
                    opp_val = getattr(item, "afpText_triplet174", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet174", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet174"):
                    opp_val = getattr(item, "afpText_triplet174", None)
                    
                    setattr(item, "afpText_triplet174", self)
                    

    @property
    def afpText_MMDRG(self):
        return self.__afpText_MMDRG

    @afpText_MMDRG.setter
    def afpText_MMDRG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MMDRG__afpText_MMDRG", None)
        self.__afpText_MMDRG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_MMD"):
                opp_val = getattr(old_value, "afpText_MMD", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_MMD"):
                opp_val = getattr(value, "afpText_MMD", None)
                if opp_val is None:
                    setattr(value, "afpText_MMD", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_MMCRG:

    def __init__(self, key: str, value: str, afpText_MMCRG: "afpText_MMC" = None):
        self.key = key
        self.value = value
        self.afpText_MMCRG = afpText_MMCRG
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def afpText_MMCRG(self):
        return self.__afpText_MMCRG

    @afpText_MMCRG.setter
    def afpText_MMCRG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MMCRG__afpText_MMCRG", None)
        self.__afpText_MMCRG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_MMC"):
                opp_val = getattr(old_value, "afpText_MMC", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_MMC"):
                opp_val = getattr(value, "afpText_MMC", None)
                if opp_val is None:
                    setattr(value, "afpText_MMC", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_MCCRG:

    def __init__(self, Startnum: str, Stopnum: str, MMCid: str, afpText_MCCRG: "afpText_MCC" = None):
        self.Startnum = Startnum
        self.Stopnum = Stopnum
        self.MMCid = MMCid
        self.afpText_MCCRG = afpText_MCCRG
        
    @property
    def Startnum(self) -> str:
        return self.__Startnum

    @Startnum.setter
    def Startnum(self, Startnum: str):
        self.__Startnum = Startnum

    @property
    def MMCid(self) -> str:
        return self.__MMCid

    @MMCid.setter
    def MMCid(self, MMCid: str):
        self.__MMCid = MMCid

    @property
    def Stopnum(self) -> str:
        return self.__Stopnum

    @Stopnum.setter
    def Stopnum(self, Stopnum: str):
        self.__Stopnum = Stopnum

    @property
    def afpText_MCCRG(self):
        return self.__afpText_MCCRG

    @afpText_MCCRG.setter
    def afpText_MCCRG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MCCRG__afpText_MCCRG", None)
        self.__afpText_MCCRG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_MCC"):
                opp_val = getattr(old_value, "afpText_MCC", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_MCC"):
                opp_val = getattr(value, "afpText_MCC", None)
                if opp_val is None:
                    setattr(value, "afpText_MCC", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_MCARG:

    def __init__(self, RGLength: str, afpText_MCARG: "afpText_MCA" = None, afpText_MCARG158: set["afpText_triplet"] = None):
        self.RGLength = RGLength
        self.afpText_MCARG = afpText_MCARG
        self.afpText_MCARG158 = afpText_MCARG158 if afpText_MCARG158 is not None else set()
        
    @property
    def RGLength(self) -> str:
        return self.__RGLength

    @RGLength.setter
    def RGLength(self, RGLength: str):
        self.__RGLength = RGLength

    @property
    def afpText_MCARG158(self):
        return self.__afpText_MCARG158

    @afpText_MCARG158.setter
    def afpText_MCARG158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MCARG__afpText_MCARG158", None)
        self.__afpText_MCARG158 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet159"):
                    opp_val = getattr(item, "afpText_triplet159", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet159", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet159"):
                    opp_val = getattr(item, "afpText_triplet159", None)
                    
                    setattr(item, "afpText_triplet159", self)
                    

    @property
    def afpText_MCARG(self):
        return self.__afpText_MCARG

    @afpText_MCARG.setter
    def afpText_MCARG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MCARG__afpText_MCARG", None)
        self.__afpText_MCARG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_MCA"):
                opp_val = getattr(old_value, "afpText_MCA", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_MCA"):
                opp_val = getattr(value, "afpText_MCA", None)
                if opp_val is None:
                    setattr(value, "afpText_MCA", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_MBCRG:

    def __init__(self, RGLength: str, afpText_MBCRG: "afpText_MBC" = None, afpText_MBCRG155: set["afpText_triplet"] = None):
        self.RGLength = RGLength
        self.afpText_MBCRG = afpText_MBCRG
        self.afpText_MBCRG155 = afpText_MBCRG155 if afpText_MBCRG155 is not None else set()
        
    @property
    def RGLength(self) -> str:
        return self.__RGLength

    @RGLength.setter
    def RGLength(self, RGLength: str):
        self.__RGLength = RGLength

    @property
    def afpText_MBCRG155(self):
        return self.__afpText_MBCRG155

    @afpText_MBCRG155.setter
    def afpText_MBCRG155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MBCRG__afpText_MBCRG155", None)
        self.__afpText_MBCRG155 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet156"):
                    opp_val = getattr(item, "afpText_triplet156", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet156", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet156"):
                    opp_val = getattr(item, "afpText_triplet156", None)
                    
                    setattr(item, "afpText_triplet156", self)
                    

    @property
    def afpText_MBCRG(self):
        return self.__afpText_MBCRG

    @afpText_MBCRG.setter
    def afpText_MBCRG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MBCRG__afpText_MBCRG", None)
        self.__afpText_MBCRG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_MBC"):
                opp_val = getattr(old_value, "afpText_MBC", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_MBC"):
                opp_val = getattr(value, "afpText_MBC", None)
                if opp_val is None:
                    setattr(value, "afpText_MBC", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_MCF1RG:

    def __init__(self, FCSName: str, CharRot: str, CFLid: str, Sectid: str, CFName: str, CPName: str, afpText_MCF1RG: "afpText_MCF1" = None):
        self.FCSName = FCSName
        self.CharRot = CharRot
        self.CFLid = CFLid
        self.Sectid = Sectid
        self.CFName = CFName
        self.CPName = CPName
        self.afpText_MCF1RG = afpText_MCF1RG
        
    @property
    def CPName(self) -> str:
        return self.__CPName

    @CPName.setter
    def CPName(self, CPName: str):
        self.__CPName = CPName

    @property
    def FCSName(self) -> str:
        return self.__FCSName

    @FCSName.setter
    def FCSName(self, FCSName: str):
        self.__FCSName = FCSName

    @property
    def CharRot(self) -> str:
        return self.__CharRot

    @CharRot.setter
    def CharRot(self, CharRot: str):
        self.__CharRot = CharRot

    @property
    def Sectid(self) -> str:
        return self.__Sectid

    @Sectid.setter
    def Sectid(self, Sectid: str):
        self.__Sectid = Sectid

    @property
    def CFName(self) -> str:
        return self.__CFName

    @CFName.setter
    def CFName(self, CFName: str):
        self.__CFName = CFName

    @property
    def CFLid(self) -> str:
        return self.__CFLid

    @CFLid.setter
    def CFLid(self, CFLid: str):
        self.__CFLid = CFLid

    @property
    def afpText_MCF1RG(self):
        return self.__afpText_MCF1RG

    @afpText_MCF1RG.setter
    def afpText_MCF1RG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MCF1RG__afpText_MCF1RG", None)
        self.__afpText_MCF1RG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_MCF1"):
                opp_val = getattr(old_value, "afpText_MCF1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_MCF1"):
                opp_val = getattr(value, "afpText_MCF1", None)
                if opp_val is None:
                    setattr(value, "afpText_MCF1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_MCFRG:

    def __init__(self, RGLength: str, afpText_MCFRG: "afpText_MCF" = None, afpText_MCFRG152: set["afpText_triplet"] = None):
        self.RGLength = RGLength
        self.afpText_MCFRG = afpText_MCFRG
        self.afpText_MCFRG152 = afpText_MCFRG152 if afpText_MCFRG152 is not None else set()
        
    @property
    def RGLength(self) -> str:
        return self.__RGLength

    @RGLength.setter
    def RGLength(self, RGLength: str):
        self.__RGLength = RGLength

    @property
    def afpText_MCFRG(self):
        return self.__afpText_MCFRG

    @afpText_MCFRG.setter
    def afpText_MCFRG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MCFRG__afpText_MCFRG", None)
        self.__afpText_MCFRG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_MCF"):
                opp_val = getattr(old_value, "afpText_MCF", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_MCF"):
                opp_val = getattr(value, "afpText_MCF", None)
                if opp_val is None:
                    setattr(value, "afpText_MCF", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def afpText_MCFRG152(self):
        return self.__afpText_MCFRG152

    @afpText_MCFRG152.setter
    def afpText_MCFRG152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MCFRG__afpText_MCFRG152", None)
        self.__afpText_MCFRG152 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet153"):
                    opp_val = getattr(item, "afpText_triplet153", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet153", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet153"):
                    opp_val = getattr(item, "afpText_triplet153", None)
                    
                    setattr(item, "afpText_triplet153", self)
                    

class afpText_MCDRG:

    def __init__(self, RGLength: str, afpText_MCDRG: "afpText_MCD" = None, afpText_MCDRG161: set["afpText_triplet"] = None):
        self.RGLength = RGLength
        self.afpText_MCDRG = afpText_MCDRG
        self.afpText_MCDRG161 = afpText_MCDRG161 if afpText_MCDRG161 is not None else set()
        
    @property
    def RGLength(self) -> str:
        return self.__RGLength

    @RGLength.setter
    def RGLength(self, RGLength: str):
        self.__RGLength = RGLength

    @property
    def afpText_MCDRG(self):
        return self.__afpText_MCDRG

    @afpText_MCDRG.setter
    def afpText_MCDRG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MCDRG__afpText_MCDRG", None)
        self.__afpText_MCDRG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_MCD"):
                opp_val = getattr(old_value, "afpText_MCD", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_MCD"):
                opp_val = getattr(value, "afpText_MCD", None)
                if opp_val is None:
                    setattr(value, "afpText_MCD", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def afpText_MCDRG161(self):
        return self.__afpText_MCDRG161

    @afpText_MCDRG161.setter
    def afpText_MCDRG161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MCDRG__afpText_MCDRG161", None)
        self.__afpText_MCDRG161 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet162"):
                    opp_val = getattr(item, "afpText_triplet162", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet162", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet162"):
                    opp_val = getattr(item, "afpText_triplet162", None)
                    
                    setattr(item, "afpText_triplet162", self)
                    

class afpText_LLERG:

    def __init__(self, RGLength: str, RGFunct: str, afpText_LLERG: "afpText_LLE" = None, afpText_LLERG149: set["afpText_triplet"] = None):
        self.RGLength = RGLength
        self.RGFunct = RGFunct
        self.afpText_LLERG = afpText_LLERG
        self.afpText_LLERG149 = afpText_LLERG149 if afpText_LLERG149 is not None else set()
        
    @property
    def RGFunct(self) -> str:
        return self.__RGFunct

    @RGFunct.setter
    def RGFunct(self, RGFunct: str):
        self.__RGFunct = RGFunct

    @property
    def RGLength(self) -> str:
        return self.__RGLength

    @RGLength.setter
    def RGLength(self, RGLength: str):
        self.__RGLength = RGLength

    @property
    def afpText_LLERG(self):
        return self.__afpText_LLERG

    @afpText_LLERG.setter
    def afpText_LLERG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_LLERG__afpText_LLERG", None)
        self.__afpText_LLERG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_LLE"):
                opp_val = getattr(old_value, "afpText_LLE", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_LLE"):
                opp_val = getattr(value, "afpText_LLE", None)
                if opp_val is None:
                    setattr(value, "afpText_LLE", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def afpText_LLERG149(self):
        return self.__afpText_LLERG149

    @afpText_LLERG149.setter
    def afpText_LLERG149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_LLERG__afpText_LLERG149", None)
        self.__afpText_LLERG149 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet150"):
                    opp_val = getattr(item, "afpText_triplet150", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet150", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet150"):
                    opp_val = getattr(item, "afpText_triplet150", None)
                    
                    setattr(item, "afpText_triplet150", self)
                    

class afpText_FNPRG:

    def __init__(self, Retired: str, Reserved3: str, UscoreWd: str, UscoreWdf: str, UscorePos: str, Reserved: str, LcHeight: str, CapMHt: str, MaxAscHt: str, MaxDesDp: str, Reserved2: str, afpText_FNPRG: "afpText_FNP" = None):
        self.Retired = Retired
        self.Reserved3 = Reserved3
        self.UscoreWd = UscoreWd
        self.UscoreWdf = UscoreWdf
        self.UscorePos = UscorePos
        self.Reserved = Reserved
        self.LcHeight = LcHeight
        self.CapMHt = CapMHt
        self.MaxAscHt = MaxAscHt
        self.MaxDesDp = MaxDesDp
        self.Reserved2 = Reserved2
        self.afpText_FNPRG = afpText_FNPRG
        
    @property
    def Reserved3(self) -> str:
        return self.__Reserved3

    @Reserved3.setter
    def Reserved3(self, Reserved3: str):
        self.__Reserved3 = Reserved3

    @property
    def MaxAscHt(self) -> str:
        return self.__MaxAscHt

    @MaxAscHt.setter
    def MaxAscHt(self, MaxAscHt: str):
        self.__MaxAscHt = MaxAscHt

    @property
    def Reserved2(self) -> str:
        return self.__Reserved2

    @Reserved2.setter
    def Reserved2(self, Reserved2: str):
        self.__Reserved2 = Reserved2

    @property
    def Reserved(self) -> str:
        return self.__Reserved

    @Reserved.setter
    def Reserved(self, Reserved: str):
        self.__Reserved = Reserved

    @property
    def MaxDesDp(self) -> str:
        return self.__MaxDesDp

    @MaxDesDp.setter
    def MaxDesDp(self, MaxDesDp: str):
        self.__MaxDesDp = MaxDesDp

    @property
    def UscoreWdf(self) -> str:
        return self.__UscoreWdf

    @UscoreWdf.setter
    def UscoreWdf(self, UscoreWdf: str):
        self.__UscoreWdf = UscoreWdf

    @property
    def CapMHt(self) -> str:
        return self.__CapMHt

    @CapMHt.setter
    def CapMHt(self, CapMHt: str):
        self.__CapMHt = CapMHt

    @property
    def UscoreWd(self) -> str:
        return self.__UscoreWd

    @UscoreWd.setter
    def UscoreWd(self, UscoreWd: str):
        self.__UscoreWd = UscoreWd

    @property
    def UscorePos(self) -> str:
        return self.__UscorePos

    @UscorePos.setter
    def UscorePos(self, UscorePos: str):
        self.__UscorePos = UscorePos

    @property
    def LcHeight(self) -> str:
        return self.__LcHeight

    @LcHeight.setter
    def LcHeight(self, LcHeight: str):
        self.__LcHeight = LcHeight

    @property
    def Retired(self) -> str:
        return self.__Retired

    @Retired.setter
    def Retired(self, Retired: str):
        self.__Retired = Retired

    @property
    def afpText_FNPRG(self):
        return self.__afpText_FNPRG

    @afpText_FNPRG.setter
    def afpText_FNPRG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_FNPRG__afpText_FNPRG", None)
        self.__afpText_FNPRG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_FNP"):
                opp_val = getattr(old_value, "afpText_FNP", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_FNP"):
                opp_val = getattr(value, "afpText_FNP", None)
                if opp_val is None:
                    setattr(value, "afpText_FNP", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_FNORG:

    def __init__(self, Reserved: str, CharRot: str, MaxBOset: str, MaxCharInc: str, SpCharInc: str, MaxBExt: str, OrntFlgs: str, Reserved2: str, EmSpInc: str, Reserved3: str, FigSpInc: str, NomCharInc: str, DefBInc: str, MinASp: str, afpText_FNORG: "afpText_FNO" = None):
        self.Reserved = Reserved
        self.CharRot = CharRot
        self.MaxBOset = MaxBOset
        self.MaxCharInc = MaxCharInc
        self.SpCharInc = SpCharInc
        self.MaxBExt = MaxBExt
        self.OrntFlgs = OrntFlgs
        self.Reserved2 = Reserved2
        self.EmSpInc = EmSpInc
        self.Reserved3 = Reserved3
        self.FigSpInc = FigSpInc
        self.NomCharInc = NomCharInc
        self.DefBInc = DefBInc
        self.MinASp = MinASp
        self.afpText_FNORG = afpText_FNORG
        
    @property
    def MaxCharInc(self) -> str:
        return self.__MaxCharInc

    @MaxCharInc.setter
    def MaxCharInc(self, MaxCharInc: str):
        self.__MaxCharInc = MaxCharInc

    @property
    def Reserved2(self) -> str:
        return self.__Reserved2

    @Reserved2.setter
    def Reserved2(self, Reserved2: str):
        self.__Reserved2 = Reserved2

    @property
    def Reserved3(self) -> str:
        return self.__Reserved3

    @Reserved3.setter
    def Reserved3(self, Reserved3: str):
        self.__Reserved3 = Reserved3

    @property
    def MinASp(self) -> str:
        return self.__MinASp

    @MinASp.setter
    def MinASp(self, MinASp: str):
        self.__MinASp = MinASp

    @property
    def MaxBExt(self) -> str:
        return self.__MaxBExt

    @MaxBExt.setter
    def MaxBExt(self, MaxBExt: str):
        self.__MaxBExt = MaxBExt

    @property
    def CharRot(self) -> str:
        return self.__CharRot

    @CharRot.setter
    def CharRot(self, CharRot: str):
        self.__CharRot = CharRot

    @property
    def DefBInc(self) -> str:
        return self.__DefBInc

    @DefBInc.setter
    def DefBInc(self, DefBInc: str):
        self.__DefBInc = DefBInc

    @property
    def Reserved(self) -> str:
        return self.__Reserved

    @Reserved.setter
    def Reserved(self, Reserved: str):
        self.__Reserved = Reserved

    @property
    def FigSpInc(self) -> str:
        return self.__FigSpInc

    @FigSpInc.setter
    def FigSpInc(self, FigSpInc: str):
        self.__FigSpInc = FigSpInc

    @property
    def NomCharInc(self) -> str:
        return self.__NomCharInc

    @NomCharInc.setter
    def NomCharInc(self, NomCharInc: str):
        self.__NomCharInc = NomCharInc

    @property
    def OrntFlgs(self) -> str:
        return self.__OrntFlgs

    @OrntFlgs.setter
    def OrntFlgs(self, OrntFlgs: str):
        self.__OrntFlgs = OrntFlgs

    @property
    def EmSpInc(self) -> str:
        return self.__EmSpInc

    @EmSpInc.setter
    def EmSpInc(self, EmSpInc: str):
        self.__EmSpInc = EmSpInc

    @property
    def MaxBOset(self) -> str:
        return self.__MaxBOset

    @MaxBOset.setter
    def MaxBOset(self, MaxBOset: str):
        self.__MaxBOset = MaxBOset

    @property
    def SpCharInc(self) -> str:
        return self.__SpCharInc

    @SpCharInc.setter
    def SpCharInc(self, SpCharInc: str):
        self.__SpCharInc = SpCharInc

    @property
    def afpText_FNORG(self):
        return self.__afpText_FNORG

    @afpText_FNORG.setter
    def afpText_FNORG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_FNORG__afpText_FNORG", None)
        self.__afpText_FNORG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_FNO"):
                opp_val = getattr(old_value, "afpText_FNO", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_FNO"):
                opp_val = getattr(value, "afpText_FNO", None)
                if opp_val is None:
                    setattr(value, "afpText_FNO", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_FNMRG:

    def __init__(self, CharBoxWd: str, CharBoxHt: str, PatDOset: str, afpText_FNMRG: "afpText_FNM" = None):
        self.CharBoxWd = CharBoxWd
        self.CharBoxHt = CharBoxHt
        self.PatDOset = PatDOset
        self.afpText_FNMRG = afpText_FNMRG
        
    @property
    def PatDOset(self) -> str:
        return self.__PatDOset

    @PatDOset.setter
    def PatDOset(self, PatDOset: str):
        self.__PatDOset = PatDOset

    @property
    def CharBoxHt(self) -> str:
        return self.__CharBoxHt

    @CharBoxHt.setter
    def CharBoxHt(self, CharBoxHt: str):
        self.__CharBoxHt = CharBoxHt

    @property
    def CharBoxWd(self) -> str:
        return self.__CharBoxWd

    @CharBoxWd.setter
    def CharBoxWd(self, CharBoxWd: str):
        self.__CharBoxWd = CharBoxWd

    @property
    def afpText_FNMRG(self):
        return self.__afpText_FNMRG

    @afpText_FNMRG.setter
    def afpText_FNMRG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_FNMRG__afpText_FNMRG", None)
        self.__afpText_FNMRG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_FNM"):
                opp_val = getattr(old_value, "afpText_FNM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_FNM"):
                opp_val = getattr(value, "afpText_FNM", None)
                if opp_val is None:
                    setattr(value, "afpText_FNM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_FNIRG:

    def __init__(self, GCGID: str, CharInc: str, AscendHt: str, DescendDp: str, Reserved: str, FNMCnt: str, ASpace: str, BSpace: str, CSpace: str, Reserved2: str, BaseOset: str, afpText_FNIRG: "afpText_FNI" = None):
        self.GCGID = GCGID
        self.CharInc = CharInc
        self.AscendHt = AscendHt
        self.DescendDp = DescendDp
        self.Reserved = Reserved
        self.FNMCnt = FNMCnt
        self.ASpace = ASpace
        self.BSpace = BSpace
        self.CSpace = CSpace
        self.Reserved2 = Reserved2
        self.BaseOset = BaseOset
        self.afpText_FNIRG = afpText_FNIRG
        
    @property
    def CSpace(self) -> str:
        return self.__CSpace

    @CSpace.setter
    def CSpace(self, CSpace: str):
        self.__CSpace = CSpace

    @property
    def BSpace(self) -> str:
        return self.__BSpace

    @BSpace.setter
    def BSpace(self, BSpace: str):
        self.__BSpace = BSpace

    @property
    def Reserved2(self) -> str:
        return self.__Reserved2

    @Reserved2.setter
    def Reserved2(self, Reserved2: str):
        self.__Reserved2 = Reserved2

    @property
    def Reserved(self) -> str:
        return self.__Reserved

    @Reserved.setter
    def Reserved(self, Reserved: str):
        self.__Reserved = Reserved

    @property
    def FNMCnt(self) -> str:
        return self.__FNMCnt

    @FNMCnt.setter
    def FNMCnt(self, FNMCnt: str):
        self.__FNMCnt = FNMCnt

    @property
    def DescendDp(self) -> str:
        return self.__DescendDp

    @DescendDp.setter
    def DescendDp(self, DescendDp: str):
        self.__DescendDp = DescendDp

    @property
    def AscendHt(self) -> str:
        return self.__AscendHt

    @AscendHt.setter
    def AscendHt(self, AscendHt: str):
        self.__AscendHt = AscendHt

    @property
    def GCGID(self) -> str:
        return self.__GCGID

    @GCGID.setter
    def GCGID(self, GCGID: str):
        self.__GCGID = GCGID

    @property
    def BaseOset(self) -> str:
        return self.__BaseOset

    @BaseOset.setter
    def BaseOset(self, BaseOset: str):
        self.__BaseOset = BaseOset

    @property
    def ASpace(self) -> str:
        return self.__ASpace

    @ASpace.setter
    def ASpace(self, ASpace: str):
        self.__ASpace = ASpace

    @property
    def CharInc(self) -> str:
        return self.__CharInc

    @CharInc.setter
    def CharInc(self, CharInc: str):
        self.__CharInc = CharInc

    @property
    def afpText_FNIRG(self):
        return self.__afpText_FNIRG

    @afpText_FNIRG.setter
    def afpText_FNIRG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_FNIRG__afpText_FNIRG", None)
        self.__afpText_FNIRG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_FNI"):
                opp_val = getattr(old_value, "afpText_FNI", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_FNI"):
                opp_val = getattr(value, "afpText_FNI", None)
                if opp_val is None:
                    setattr(value, "afpText_FNI", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_CPIRG:

    def __init__(self, GCGID: str, PrtFlags: str, CodePoint: str, Count: str, afpText_CPIRG: "afpText_CPI" = None):
        self.GCGID = GCGID
        self.PrtFlags = PrtFlags
        self.CodePoint = CodePoint
        self.Count = Count
        self.afpText_CPIRG = afpText_CPIRG
        
    @property
    def CodePoint(self) -> str:
        return self.__CodePoint

    @CodePoint.setter
    def CodePoint(self, CodePoint: str):
        self.__CodePoint = CodePoint

    @property
    def PrtFlags(self) -> str:
        return self.__PrtFlags

    @PrtFlags.setter
    def PrtFlags(self, PrtFlags: str):
        self.__PrtFlags = PrtFlags

    @property
    def GCGID(self) -> str:
        return self.__GCGID

    @GCGID.setter
    def GCGID(self, GCGID: str):
        self.__GCGID = GCGID

    @property
    def Count(self) -> str:
        return self.__Count

    @Count.setter
    def Count(self, Count: str):
        self.__Count = Count

    @property
    def afpText_CPIRG(self):
        return self.__afpText_CPIRG

    @afpText_CPIRG.setter
    def afpText_CPIRG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_CPIRG__afpText_CPIRG", None)
        self.__afpText_CPIRG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_CPI"):
                opp_val = getattr(old_value, "afpText_CPI", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_CPI"):
                opp_val = getattr(value, "afpText_CPI", None)
                if opp_val is None:
                    setattr(value, "afpText_CPI", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_CFIRG:

    def __init__(self, FCSName: str, CPName: str, SVSize: str, SHScale: str, Reserved: str, Section: str, afpText_CFIRG: "afpText_CFI" = None):
        self.FCSName = FCSName
        self.CPName = CPName
        self.SVSize = SVSize
        self.SHScale = SHScale
        self.Reserved = Reserved
        self.Section = Section
        self.afpText_CFIRG = afpText_CFIRG
        
    @property
    def SHScale(self) -> str:
        return self.__SHScale

    @SHScale.setter
    def SHScale(self, SHScale: str):
        self.__SHScale = SHScale

    @property
    def CPName(self) -> str:
        return self.__CPName

    @CPName.setter
    def CPName(self, CPName: str):
        self.__CPName = CPName

    @property
    def SVSize(self) -> str:
        return self.__SVSize

    @SVSize.setter
    def SVSize(self, SVSize: str):
        self.__SVSize = SVSize

    @property
    def FCSName(self) -> str:
        return self.__FCSName

    @FCSName.setter
    def FCSName(self, FCSName: str):
        self.__FCSName = FCSName

    @property
    def Section(self) -> str:
        return self.__Section

    @Section.setter
    def Section(self, Section: str):
        self.__Section = Section

    @property
    def Reserved(self) -> str:
        return self.__Reserved

    @Reserved.setter
    def Reserved(self, Reserved: str):
        self.__Reserved = Reserved

    @property
    def afpText_CFIRG(self):
        return self.__afpText_CFIRG

    @afpText_CFIRG.setter
    def afpText_CFIRG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_CFIRG__afpText_CFIRG", None)
        self.__afpText_CFIRG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afpText_CFI"):
                opp_val = getattr(old_value, "afpText_CFI", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afpText_CFI"):
                opp_val = getattr(value, "afpText_CFI", None)
                if opp_val is None:
                    setattr(value, "afpText_CFI", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afpText_Model:

    pass
class afpText_triplet:

    pass
class structuredField:

    pass
class afpText_PTX(structuredField):

    pass
class afpText_EDX(structuredField):

    def __init__(self, DMXName: str):
        self.DMXName = DMXName
        
    @property
    def DMXName(self) -> str:
        return self.__DMXName

    @DMXName.setter
    def DMXName(self, DMXName: str):
        self.__DMXName = DMXName

class afpText_EFM(structuredField):

    def __init__(self, FMName: str):
        self.FMName = FMName
        
    @property
    def FMName(self) -> str:
        return self.__FMName

    @FMName.setter
    def FMName(self, FMName: str):
        self.__FMName = FMName

class afpText_ENG(structuredField):

    def __init__(self, PGrpName: str, afpText_ENG: set["afpText_triplet"] = None):
        self.PGrpName = PGrpName
        self.afpText_ENG = afpText_ENG if afpText_ENG is not None else set()
        
    @property
    def PGrpName(self) -> str:
        return self.__PGrpName

    @PGrpName.setter
    def PGrpName(self, PGrpName: str):
        self.__PGrpName = PGrpName

    @property
    def afpText_ENG(self):
        return self.__afpText_ENG

    @afpText_ENG.setter
    def afpText_ENG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_ENG__afpText_ENG", None)
        self.__afpText_ENG = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet71"):
                    opp_val = getattr(item, "afpText_triplet71", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet71"):
                    opp_val = getattr(item, "afpText_triplet71", None)
                    
                    setattr(item, "afpText_triplet71", self)
                    

class afpText_BAG(structuredField):

    def __init__(self, AEGName: str, afpText_BAG: set["afpText_triplet"] = None):
        self.AEGName = AEGName
        self.afpText_BAG = afpText_BAG if afpText_BAG is not None else set()
        
    @property
    def AEGName(self) -> str:
        return self.__AEGName

    @AEGName.setter
    def AEGName(self, AEGName: str):
        self.__AEGName = AEGName

    @property
    def afpText_BAG(self):
        return self.__afpText_BAG

    @afpText_BAG.setter
    def afpText_BAG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_BAG__afpText_BAG", None)
        self.__afpText_BAG = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet"):
                    opp_val = getattr(item, "afpText_triplet", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet"):
                    opp_val = getattr(item, "afpText_triplet", None)
                    
                    setattr(item, "afpText_triplet", self)
                    

class afpText_MCD(structuredField):

    pass
class afpText_BDI(structuredField):

    def __init__(self, IndxName: str, afpText_BDI: set["afpText_triplet"] = None):
        self.IndxName = IndxName
        self.afpText_BDI = afpText_BDI if afpText_BDI is not None else set()
        
    @property
    def IndxName(self) -> str:
        return self.__IndxName

    @IndxName.setter
    def IndxName(self, IndxName: str):
        self.__IndxName = IndxName

    @property
    def afpText_BDI(self):
        return self.__afpText_BDI

    @afpText_BDI.setter
    def afpText_BDI(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_BDI__afpText_BDI", None)
        self.__afpText_BDI = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet13"):
                    opp_val = getattr(item, "afpText_triplet13", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet13"):
                    opp_val = getattr(item, "afpText_triplet13", None)
                    
                    setattr(item, "afpText_triplet13", self)
                    

class afpText_EPM(structuredField):

    def __init__(self, PMName: str):
        self.PMName = PMName
        
    @property
    def PMName(self) -> str:
        return self.__PMName

    @PMName.setter
    def PMName(self, PMName: str):
        self.__PMName = PMName

class afpText_BDG(structuredField):

    def __init__(self, DEGName: str, afpText_BDG: set["afpText_triplet"] = None):
        self.DEGName = DEGName
        self.afpText_BDG = afpText_BDG if afpText_BDG is not None else set()
        
    @property
    def DEGName(self) -> str:
        return self.__DEGName

    @DEGName.setter
    def DEGName(self, DEGName: str):
        self.__DEGName = DEGName

    @property
    def afpText_BDG(self):
        return self.__afpText_BDG

    @afpText_BDG.setter
    def afpText_BDG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_BDG__afpText_BDG", None)
        self.__afpText_BDG = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet11"):
                    opp_val = getattr(item, "afpText_triplet11", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet11"):
                    opp_val = getattr(item, "afpText_triplet11", None)
                    
                    setattr(item, "afpText_triplet11", self)
                    

class afpText_EIM(structuredField):

    def __init__(self, IdoName: str, afpText_EIM: set["afpText_triplet"] = None):
        self.IdoName = IdoName
        self.afpText_EIM = afpText_EIM if afpText_EIM is not None else set()
        
    @property
    def IdoName(self) -> str:
        return self.__IdoName

    @IdoName.setter
    def IdoName(self, IdoName: str):
        self.__IdoName = IdoName

    @property
    def afpText_EIM(self):
        return self.__afpText_EIM

    @afpText_EIM.setter
    def afpText_EIM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_EIM__afpText_EIM", None)
        self.__afpText_EIM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet67"):
                    opp_val = getattr(item, "afpText_triplet67", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet67"):
                    opp_val = getattr(item, "afpText_triplet67", None)
                    
                    setattr(item, "afpText_triplet67", self)
                    

class afpText_MBC(structuredField):

    pass
class afpText_EPT(structuredField):

    def __init__(self, PTdoName: str, afpText_EPT: set["afpText_triplet"] = None):
        self.PTdoName = PTdoName
        self.afpText_EPT = afpText_EPT if afpText_EPT is not None else set()
        
    @property
    def PTdoName(self) -> str:
        return self.__PTdoName

    @PTdoName.setter
    def PTdoName(self, PTdoName: str):
        self.__PTdoName = PTdoName

    @property
    def afpText_EPT(self):
        return self.__afpText_EPT

    @afpText_EPT.setter
    def afpText_EPT(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_EPT__afpText_EPT", None)
        self.__afpText_EPT = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet79"):
                    opp_val = getattr(item, "afpText_triplet79", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet79"):
                    opp_val = getattr(item, "afpText_triplet79", None)
                    
                    setattr(item, "afpText_triplet79", self)
                    

class afpText_BBC(structuredField):

    def __init__(self, BCdoName: str, afpText_BBC: set["afpText_triplet"] = None):
        self.BCdoName = BCdoName
        self.afpText_BBC = afpText_BBC if afpText_BBC is not None else set()
        
    @property
    def BCdoName(self) -> str:
        return self.__BCdoName

    @BCdoName.setter
    def BCdoName(self, BCdoName: str):
        self.__BCdoName = BCdoName

    @property
    def afpText_BBC(self):
        return self.__afpText_BBC

    @afpText_BBC.setter
    def afpText_BBC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_BBC__afpText_BBC", None)
        self.__afpText_BBC = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet3"):
                    opp_val = getattr(item, "afpText_triplet3", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet3"):
                    opp_val = getattr(item, "afpText_triplet3", None)
                    
                    setattr(item, "afpText_triplet3", self)
                    

class afpText_EMO(structuredField):

    def __init__(self, OvlyName: str, afpText_EMO: set["afpText_triplet"] = None):
        self.OvlyName = OvlyName
        self.afpText_EMO = afpText_EMO if afpText_EMO is not None else set()
        
    @property
    def OvlyName(self) -> str:
        return self.__OvlyName

    @OvlyName.setter
    def OvlyName(self, OvlyName: str):
        self.__OvlyName = OvlyName

    @property
    def afpText_EMO(self):
        return self.__afpText_EMO

    @afpText_EMO.setter
    def afpText_EMO(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_EMO__afpText_EMO", None)
        self.__afpText_EMO = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet69"):
                    opp_val = getattr(item, "afpText_triplet69", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet69"):
                    opp_val = getattr(item, "afpText_triplet69", None)
                    
                    setattr(item, "afpText_triplet69", self)
                    

class afpText_OCD(structuredField):

    def __init__(self, ObjCdat: str):
        self.ObjCdat = ObjCdat
        
    @property
    def ObjCdat(self) -> str:
        return self.__ObjCdat

    @ObjCdat.setter
    def ObjCdat(self, ObjCdat: str):
        self.__ObjCdat = ObjCdat

class afpText_IID(structuredField):

    def __init__(self, ConData1: str, XBase: str, YBase: str, XUnits: str, YUnits: str, XSize: str, YSize: str, ConData2: str, XCSizeD: str, YCSizeD: str, ConData3: str, Color: str):
        self.ConData1 = ConData1
        self.XBase = XBase
        self.YBase = YBase
        self.XUnits = XUnits
        self.YUnits = YUnits
        self.XSize = XSize
        self.YSize = YSize
        self.ConData2 = ConData2
        self.XCSizeD = XCSizeD
        self.YCSizeD = YCSizeD
        self.ConData3 = ConData3
        self.Color = Color
        
    @property
    def XBase(self) -> str:
        return self.__XBase

    @XBase.setter
    def XBase(self, XBase: str):
        self.__XBase = XBase

    @property
    def ConData1(self) -> str:
        return self.__ConData1

    @ConData1.setter
    def ConData1(self, ConData1: str):
        self.__ConData1 = ConData1

    @property
    def YCSizeD(self) -> str:
        return self.__YCSizeD

    @YCSizeD.setter
    def YCSizeD(self, YCSizeD: str):
        self.__YCSizeD = YCSizeD

    @property
    def YBase(self) -> str:
        return self.__YBase

    @YBase.setter
    def YBase(self, YBase: str):
        self.__YBase = YBase

    @property
    def XUnits(self) -> str:
        return self.__XUnits

    @XUnits.setter
    def XUnits(self, XUnits: str):
        self.__XUnits = XUnits

    @property
    def YUnits(self) -> str:
        return self.__YUnits

    @YUnits.setter
    def YUnits(self, YUnits: str):
        self.__YUnits = YUnits

    @property
    def XSize(self) -> str:
        return self.__XSize

    @XSize.setter
    def XSize(self, XSize: str):
        self.__XSize = XSize

    @property
    def Color(self) -> str:
        return self.__Color

    @Color.setter
    def Color(self, Color: str):
        self.__Color = Color

    @property
    def YSize(self) -> str:
        return self.__YSize

    @YSize.setter
    def YSize(self, YSize: str):
        self.__YSize = YSize

    @property
    def XCSizeD(self) -> str:
        return self.__XCSizeD

    @XCSizeD.setter
    def XCSizeD(self, XCSizeD: str):
        self.__XCSizeD = XCSizeD

    @property
    def ConData2(self) -> str:
        return self.__ConData2

    @ConData2.setter
    def ConData2(self, ConData2: str):
        self.__ConData2 = ConData2

    @property
    def ConData3(self) -> str:
        return self.__ConData3

    @ConData3.setter
    def ConData3(self, ConData3: str):
        self.__ConData3 = ConData3

class afpText_MDR(structuredField):

    pass
class afpText_BPM(structuredField):

    def __init__(self, PMName: str):
        self.PMName = PMName
        
    @property
    def PMName(self) -> str:
        return self.__PMName

    @PMName.setter
    def PMName(self, PMName: str):
        self.__PMName = PMName

class afpText_BDT(structuredField):

    def __init__(self, DocName: str, Reserved: str, afpText_BDT: set["afpText_triplet"] = None):
        self.DocName = DocName
        self.Reserved = Reserved
        self.afpText_BDT = afpText_BDT if afpText_BDT is not None else set()
        
    @property
    def DocName(self) -> str:
        return self.__DocName

    @DocName.setter
    def DocName(self, DocName: str):
        self.__DocName = DocName

    @property
    def Reserved(self) -> str:
        return self.__Reserved

    @Reserved.setter
    def Reserved(self, Reserved: str):
        self.__Reserved = Reserved

    @property
    def afpText_BDT(self):
        return self.__afpText_BDT

    @afpText_BDT.setter
    def afpText_BDT(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_BDT__afpText_BDT", None)
        self.__afpText_BDT = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet17"):
                    opp_val = getattr(item, "afpText_triplet17", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet17"):
                    opp_val = getattr(item, "afpText_triplet17", None)
                    
                    setattr(item, "afpText_triplet17", self)
                    

class afpText_GDD(structuredField):

    def __init__(self, GOCAdes: str, afpText_GDD: set["afpText_triplet"] = None):
        self.GOCAdes = GOCAdes
        self.afpText_GDD = afpText_GDD if afpText_GDD is not None else set()
        
    @property
    def GOCAdes(self) -> str:
        return self.__GOCAdes

    @GOCAdes.setter
    def GOCAdes(self, GOCAdes: str):
        self.__GOCAdes = GOCAdes

    @property
    def afpText_GDD(self):
        return self.__afpText_GDD

    @afpText_GDD.setter
    def afpText_GDD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_GDD__afpText_GDD", None)
        self.__afpText_GDD = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet91"):
                    opp_val = getattr(item, "afpText_triplet91", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet91", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet91"):
                    opp_val = getattr(item, "afpText_triplet91", None)
                    
                    setattr(item, "afpText_triplet91", self)
                    

class afpText_BDD(structuredField):

    def __init__(self, UBASE: str, Reserved: str, XUPUB: str, YUPUB: str, XEXTENT: str, YEXTENT: str, Reserved2: str, TYPE: str, MOD: str, LID: str, COLOR: str, MODULEWIDTH: str, ELEMENTHEIGHT: str, MULT: str, WENE: str, afpText_BDD: set["afpText_triplet"] = None):
        self.UBASE = UBASE
        self.Reserved = Reserved
        self.XUPUB = XUPUB
        self.YUPUB = YUPUB
        self.XEXTENT = XEXTENT
        self.YEXTENT = YEXTENT
        self.Reserved2 = Reserved2
        self.TYPE = TYPE
        self.MOD = MOD
        self.LID = LID
        self.COLOR = COLOR
        self.MODULEWIDTH = MODULEWIDTH
        self.ELEMENTHEIGHT = ELEMENTHEIGHT
        self.MULT = MULT
        self.WENE = WENE
        self.afpText_BDD = afpText_BDD if afpText_BDD is not None else set()
        
    @property
    def WENE(self) -> str:
        return self.__WENE

    @WENE.setter
    def WENE(self, WENE: str):
        self.__WENE = WENE

    @property
    def MULT(self) -> str:
        return self.__MULT

    @MULT.setter
    def MULT(self, MULT: str):
        self.__MULT = MULT

    @property
    def XEXTENT(self) -> str:
        return self.__XEXTENT

    @XEXTENT.setter
    def XEXTENT(self, XEXTENT: str):
        self.__XEXTENT = XEXTENT

    @property
    def YEXTENT(self) -> str:
        return self.__YEXTENT

    @YEXTENT.setter
    def YEXTENT(self, YEXTENT: str):
        self.__YEXTENT = YEXTENT

    @property
    def LID(self) -> str:
        return self.__LID

    @LID.setter
    def LID(self, LID: str):
        self.__LID = LID

    @property
    def Reserved2(self) -> str:
        return self.__Reserved2

    @Reserved2.setter
    def Reserved2(self, Reserved2: str):
        self.__Reserved2 = Reserved2

    @property
    def MODULEWIDTH(self) -> str:
        return self.__MODULEWIDTH

    @MODULEWIDTH.setter
    def MODULEWIDTH(self, MODULEWIDTH: str):
        self.__MODULEWIDTH = MODULEWIDTH

    @property
    def TYPE(self) -> str:
        return self.__TYPE

    @TYPE.setter
    def TYPE(self, TYPE: str):
        self.__TYPE = TYPE

    @property
    def ELEMENTHEIGHT(self) -> str:
        return self.__ELEMENTHEIGHT

    @ELEMENTHEIGHT.setter
    def ELEMENTHEIGHT(self, ELEMENTHEIGHT: str):
        self.__ELEMENTHEIGHT = ELEMENTHEIGHT

    @property
    def XUPUB(self) -> str:
        return self.__XUPUB

    @XUPUB.setter
    def XUPUB(self, XUPUB: str):
        self.__XUPUB = XUPUB

    @property
    def Reserved(self) -> str:
        return self.__Reserved

    @Reserved.setter
    def Reserved(self, Reserved: str):
        self.__Reserved = Reserved

    @property
    def YUPUB(self) -> str:
        return self.__YUPUB

    @YUPUB.setter
    def YUPUB(self, YUPUB: str):
        self.__YUPUB = YUPUB

    @property
    def COLOR(self) -> str:
        return self.__COLOR

    @COLOR.setter
    def COLOR(self, COLOR: str):
        self.__COLOR = COLOR

    @property
    def UBASE(self) -> str:
        return self.__UBASE

    @UBASE.setter
    def UBASE(self, UBASE: str):
        self.__UBASE = UBASE

    @property
    def MOD(self) -> str:
        return self.__MOD

    @MOD.setter
    def MOD(self, MOD: str):
        self.__MOD = MOD

    @property
    def afpText_BDD(self):
        return self.__afpText_BDD

    @afpText_BDD.setter
    def afpText_BDD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_BDD__afpText_BDD", None)
        self.__afpText_BDD = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet9"):
                    opp_val = getattr(item, "afpText_triplet9", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet9"):
                    opp_val = getattr(item, "afpText_triplet9", None)
                    
                    setattr(item, "afpText_triplet9", self)
                    

class afpText_IPS(structuredField):

    def __init__(self, PsegName: str, XpsOset: str, YpsOset: str, afpText_IPS: set["afpText_triplet"] = None):
        self.PsegName = PsegName
        self.XpsOset = XpsOset
        self.YpsOset = YpsOset
        self.afpText_IPS = afpText_IPS if afpText_IPS is not None else set()
        
    @property
    def XpsOset(self) -> str:
        return self.__XpsOset

    @XpsOset.setter
    def XpsOset(self, XpsOset: str):
        self.__XpsOset = XpsOset

    @property
    def PsegName(self) -> str:
        return self.__PsegName

    @PsegName.setter
    def PsegName(self, PsegName: str):
        self.__PsegName = PsegName

    @property
    def YpsOset(self) -> str:
        return self.__YpsOset

    @YpsOset.setter
    def YpsOset(self, YpsOset: str):
        self.__YpsOset = YpsOset

    @property
    def afpText_IPS(self):
        return self.__afpText_IPS

    @afpText_IPS.setter
    def afpText_IPS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_IPS__afpText_IPS", None)
        self.__afpText_IPS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet105"):
                    opp_val = getattr(item, "afpText_triplet105", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet105"):
                    opp_val = getattr(item, "afpText_triplet105", None)
                    
                    setattr(item, "afpText_triplet105", self)
                    

class afpText_CAT(structuredField):

    def __init__(self, CATData: str):
        self.CATData = CATData
        
    @property
    def CATData(self) -> str:
        return self.__CATData

    @CATData.setter
    def CATData(self, CATData: str):
        self.__CATData = CATData

class afpText_IPD(structuredField):

    def __init__(self, IOCAdat: str, imageData: str):
        self.IOCAdat = IOCAdat
        self.imageData = imageData
        
    @property
    def IOCAdat(self) -> str:
        return self.__IOCAdat

    @IOCAdat.setter
    def IOCAdat(self, IOCAdat: str):
        self.__IOCAdat = IOCAdat

    @property
    def imageData(self) -> str:
        return self.__imageData

    @imageData.setter
    def imageData(self, imageData: str):
        self.__imageData = imageData

class afpText_EDI(structuredField):

    def __init__(self, IndxName: str, afpText_EDI: set["afpText_triplet"] = None):
        self.IndxName = IndxName
        self.afpText_EDI = afpText_EDI if afpText_EDI is not None else set()
        
    @property
    def IndxName(self) -> str:
        return self.__IndxName

    @IndxName.setter
    def IndxName(self, IndxName: str):
        self.__IndxName = IndxName

    @property
    def afpText_EDI(self):
        return self.__afpText_EDI

    @afpText_EDI.setter
    def afpText_EDI(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_EDI__afpText_EDI", None)
        self.__afpText_EDI = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet61"):
                    opp_val = getattr(item, "afpText_triplet61", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet61"):
                    opp_val = getattr(item, "afpText_triplet61", None)
                    
                    setattr(item, "afpText_triplet61", self)
                    

class afpText_PGD(structuredField):

    def __init__(self, YpgUnits: str, XpgSize: str, YpgSize: str, Reserved: str, XpgBase: str, YpgBase: str, XpgUnits: str, afpText_PGD: set["afpText_triplet"] = None):
        self.YpgUnits = YpgUnits
        self.XpgSize = XpgSize
        self.YpgSize = YpgSize
        self.Reserved = Reserved
        self.XpgBase = XpgBase
        self.YpgBase = YpgBase
        self.XpgUnits = XpgUnits
        self.afpText_PGD = afpText_PGD if afpText_PGD is not None else set()
        
    @property
    def YpgUnits(self) -> str:
        return self.__YpgUnits

    @YpgUnits.setter
    def YpgUnits(self, YpgUnits: str):
        self.__YpgUnits = YpgUnits

    @property
    def XpgUnits(self) -> str:
        return self.__XpgUnits

    @XpgUnits.setter
    def XpgUnits(self, XpgUnits: str):
        self.__XpgUnits = XpgUnits

    @property
    def XpgSize(self) -> str:
        return self.__XpgSize

    @XpgSize.setter
    def XpgSize(self, XpgSize: str):
        self.__XpgSize = XpgSize

    @property
    def YpgSize(self) -> str:
        return self.__YpgSize

    @YpgSize.setter
    def YpgSize(self, YpgSize: str):
        self.__YpgSize = YpgSize

    @property
    def Reserved(self) -> str:
        return self.__Reserved

    @Reserved.setter
    def Reserved(self, Reserved: str):
        self.__Reserved = Reserved

    @property
    def YpgBase(self) -> str:
        return self.__YpgBase

    @YpgBase.setter
    def YpgBase(self, YpgBase: str):
        self.__YpgBase = YpgBase

    @property
    def XpgBase(self) -> str:
        return self.__XpgBase

    @XpgBase.setter
    def XpgBase(self, XpgBase: str):
        self.__XpgBase = XpgBase

    @property
    def afpText_PGD(self):
        return self.__afpText_PGD

    @afpText_PGD.setter
    def afpText_PGD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_PGD__afpText_PGD", None)
        self.__afpText_PGD = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet137"):
                    opp_val = getattr(item, "afpText_triplet137", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet137", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet137"):
                    opp_val = getattr(item, "afpText_triplet137", None)
                    
                    setattr(item, "afpText_triplet137", self)
                    

class afpText_MGO(structuredField):

    pass
class afpText_EPG(structuredField):

    def __init__(self, PageName: str, afpText_EPG: set["afpText_triplet"] = None):
        self.PageName = PageName
        self.afpText_EPG = afpText_EPG if afpText_EPG is not None else set()
        
    @property
    def PageName(self) -> str:
        return self.__PageName

    @PageName.setter
    def PageName(self, PageName: str):
        self.__PageName = PageName

    @property
    def afpText_EPG(self):
        return self.__afpText_EPG

    @afpText_EPG.setter
    def afpText_EPG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_EPG__afpText_EPG", None)
        self.__afpText_EPG = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet77"):
                    opp_val = getattr(item, "afpText_triplet77", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet77", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet77"):
                    opp_val = getattr(item, "afpText_triplet77", None)
                    
                    setattr(item, "afpText_triplet77", self)
                    

class afpText_EDG(structuredField):

    def __init__(self, DEGName: str):
        self.DEGName = DEGName
        
    @property
    def DEGName(self) -> str:
        return self.__DEGName

    @DEGName.setter
    def DEGName(self, DEGName: str):
        self.__DEGName = DEGName

class afpText_EOC(structuredField):

    def __init__(self, ObjCName: str, afpText_EOC: set["afpText_triplet"] = None):
        self.ObjCName = ObjCName
        self.afpText_EOC = afpText_EOC if afpText_EOC is not None else set()
        
    @property
    def ObjCName(self) -> str:
        return self.__ObjCName

    @ObjCName.setter
    def ObjCName(self, ObjCName: str):
        self.__ObjCName = ObjCName

    @property
    def afpText_EOC(self):
        return self.__afpText_EOC

    @afpText_EOC.setter
    def afpText_EOC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_EOC__afpText_EOC", None)
        self.__afpText_EOC = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet73"):
                    opp_val = getattr(item, "afpText_triplet73", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet73"):
                    opp_val = getattr(item, "afpText_triplet73", None)
                    
                    setattr(item, "afpText_triplet73", self)
                    

class afpText_MMO(structuredField):

    def __init__(self, RGLength: str, afpText_MMO: set["afpText_MMORG"] = None):
        self.RGLength = RGLength
        self.afpText_MMO = afpText_MMO if afpText_MMO is not None else set()
        
    @property
    def RGLength(self) -> str:
        return self.__RGLength

    @RGLength.setter
    def RGLength(self, RGLength: str):
        self.__RGLength = RGLength

    @property
    def afpText_MMO(self):
        return self.__afpText_MMO

    @afpText_MMO.setter
    def afpText_MMO(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MMO__afpText_MMO", None)
        self.__afpText_MMO = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_MMORG"):
                    opp_val = getattr(item, "afpText_MMORG", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_MMORG", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_MMORG"):
                    opp_val = getattr(item, "afpText_MMORG", None)
                    
                    setattr(item, "afpText_MMORG", self)
                    

class afpText_LND(structuredField):

    def __init__(self, LNDFlgs: str, IPos: str, BPos: str, TxtOrent: str, FntLID: str, ChnlCde: str, NLNDskp: str, NLNDsp: str, NLNDreu: str, SupName: str, SOLid: str, DataStrt: str, DataLgth: str, TxtColor: str, NLNDccp: str, SubpgID: str, CCPID: str, afpText_LND: set["afpText_triplet"] = None):
        self.LNDFlgs = LNDFlgs
        self.IPos = IPos
        self.BPos = BPos
        self.TxtOrent = TxtOrent
        self.FntLID = FntLID
        self.ChnlCde = ChnlCde
        self.NLNDskp = NLNDskp
        self.NLNDsp = NLNDsp
        self.NLNDreu = NLNDreu
        self.SupName = SupName
        self.SOLid = SOLid
        self.DataStrt = DataStrt
        self.DataLgth = DataLgth
        self.TxtColor = TxtColor
        self.NLNDccp = NLNDccp
        self.SubpgID = SubpgID
        self.CCPID = CCPID
        self.afpText_LND = afpText_LND if afpText_LND is not None else set()
        
    @property
    def SupName(self) -> str:
        return self.__SupName

    @SupName.setter
    def SupName(self, SupName: str):
        self.__SupName = SupName

    @property
    def ChnlCde(self) -> str:
        return self.__ChnlCde

    @ChnlCde.setter
    def ChnlCde(self, ChnlCde: str):
        self.__ChnlCde = ChnlCde

    @property
    def NLNDsp(self) -> str:
        return self.__NLNDsp

    @NLNDsp.setter
    def NLNDsp(self, NLNDsp: str):
        self.__NLNDsp = NLNDsp

    @property
    def DataStrt(self) -> str:
        return self.__DataStrt

    @DataStrt.setter
    def DataStrt(self, DataStrt: str):
        self.__DataStrt = DataStrt

    @property
    def DataLgth(self) -> str:
        return self.__DataLgth

    @DataLgth.setter
    def DataLgth(self, DataLgth: str):
        self.__DataLgth = DataLgth

    @property
    def TxtColor(self) -> str:
        return self.__TxtColor

    @TxtColor.setter
    def TxtColor(self, TxtColor: str):
        self.__TxtColor = TxtColor

    @property
    def LNDFlgs(self) -> str:
        return self.__LNDFlgs

    @LNDFlgs.setter
    def LNDFlgs(self, LNDFlgs: str):
        self.__LNDFlgs = LNDFlgs

    @property
    def FntLID(self) -> str:
        return self.__FntLID

    @FntLID.setter
    def FntLID(self, FntLID: str):
        self.__FntLID = FntLID

    @property
    def IPos(self) -> str:
        return self.__IPos

    @IPos.setter
    def IPos(self, IPos: str):
        self.__IPos = IPos

    @property
    def BPos(self) -> str:
        return self.__BPos

    @BPos.setter
    def BPos(self, BPos: str):
        self.__BPos = BPos

    @property
    def SOLid(self) -> str:
        return self.__SOLid

    @SOLid.setter
    def SOLid(self, SOLid: str):
        self.__SOLid = SOLid

    @property
    def NLNDccp(self) -> str:
        return self.__NLNDccp

    @NLNDccp.setter
    def NLNDccp(self, NLNDccp: str):
        self.__NLNDccp = NLNDccp

    @property
    def NLNDskp(self) -> str:
        return self.__NLNDskp

    @NLNDskp.setter
    def NLNDskp(self, NLNDskp: str):
        self.__NLNDskp = NLNDskp

    @property
    def CCPID(self) -> str:
        return self.__CCPID

    @CCPID.setter
    def CCPID(self, CCPID: str):
        self.__CCPID = CCPID

    @property
    def NLNDreu(self) -> str:
        return self.__NLNDreu

    @NLNDreu.setter
    def NLNDreu(self, NLNDreu: str):
        self.__NLNDreu = NLNDreu

    @property
    def SubpgID(self) -> str:
        return self.__SubpgID

    @SubpgID.setter
    def SubpgID(self, SubpgID: str):
        self.__SubpgID = SubpgID

    @property
    def TxtOrent(self) -> str:
        return self.__TxtOrent

    @TxtOrent.setter
    def TxtOrent(self, TxtOrent: str):
        self.__TxtOrent = TxtOrent

    @property
    def afpText_LND(self):
        return self.__afpText_LND

    @afpText_LND.setter
    def afpText_LND(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_LND__afpText_LND", None)
        self.__afpText_LND = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet108"):
                    opp_val = getattr(item, "afpText_triplet108", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet108", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet108"):
                    opp_val = getattr(item, "afpText_triplet108", None)
                    
                    setattr(item, "afpText_triplet108", self)
                    

class afpText_CPI(structuredField):

    pass
class afpText_MFC(structuredField):

    def __init__(self, MFCFlgs: str, MedColl: str, MFCScpe: str, afpText_MFC: set["afpText_triplet"] = None):
        self.MFCFlgs = MFCFlgs
        self.MedColl = MedColl
        self.MFCScpe = MFCScpe
        self.afpText_MFC = afpText_MFC if afpText_MFC is not None else set()
        
    @property
    def MFCFlgs(self) -> str:
        return self.__MFCFlgs

    @MFCFlgs.setter
    def MFCFlgs(self, MFCFlgs: str):
        self.__MFCFlgs = MFCFlgs

    @property
    def MFCScpe(self) -> str:
        return self.__MFCScpe

    @MFCScpe.setter
    def MFCScpe(self, MFCScpe: str):
        self.__MFCScpe = MFCScpe

    @property
    def MedColl(self) -> str:
        return self.__MedColl

    @MedColl.setter
    def MedColl(self, MedColl: str):
        self.__MedColl = MedColl

    @property
    def afpText_MFC(self):
        return self.__afpText_MFC

    @afpText_MFC.setter
    def afpText_MFC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MFC__afpText_MFC", None)
        self.__afpText_MFC = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet119"):
                    opp_val = getattr(item, "afpText_triplet119", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet119", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet119"):
                    opp_val = getattr(item, "afpText_triplet119", None)
                    
                    setattr(item, "afpText_triplet119", self)
                    

class afpText_BSG(structuredField):

    def __init__(self, REGName: str, afpText_BSG: set["afpText_triplet"] = None):
        self.REGName = REGName
        self.afpText_BSG = afpText_BSG if afpText_BSG is not None else set()
        
    @property
    def REGName(self) -> str:
        return self.__REGName

    @REGName.setter
    def REGName(self, REGName: str):
        self.__REGName = REGName

    @property
    def afpText_BSG(self):
        return self.__afpText_BSG

    @afpText_BSG.setter
    def afpText_BSG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_BSG__afpText_BSG", None)
        self.__afpText_BSG = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet49"):
                    opp_val = getattr(item, "afpText_triplet49", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet49"):
                    opp_val = getattr(item, "afpText_triplet49", None)
                    
                    setattr(item, "afpText_triplet49", self)
                    

class afpText_PTD1(structuredField):

    def __init__(self, XPBASE: str, YPBASE: str, XPUNITVL: str, YPUNITVL: str, XPEXTENT: str, YPEXTENT: str, RESERVED: str):
        self.XPBASE = XPBASE
        self.YPBASE = YPBASE
        self.XPUNITVL = XPUNITVL
        self.YPUNITVL = YPUNITVL
        self.XPEXTENT = XPEXTENT
        self.YPEXTENT = YPEXTENT
        self.RESERVED = RESERVED
        
    @property
    def RESERVED(self) -> str:
        return self.__RESERVED

    @RESERVED.setter
    def RESERVED(self, RESERVED: str):
        self.__RESERVED = RESERVED

    @property
    def XPEXTENT(self) -> str:
        return self.__XPEXTENT

    @XPEXTENT.setter
    def XPEXTENT(self, XPEXTENT: str):
        self.__XPEXTENT = XPEXTENT

    @property
    def YPUNITVL(self) -> str:
        return self.__YPUNITVL

    @YPUNITVL.setter
    def YPUNITVL(self, YPUNITVL: str):
        self.__YPUNITVL = YPUNITVL

    @property
    def XPUNITVL(self) -> str:
        return self.__XPUNITVL

    @XPUNITVL.setter
    def XPUNITVL(self, XPUNITVL: str):
        self.__XPUNITVL = XPUNITVL

    @property
    def YPBASE(self) -> str:
        return self.__YPBASE

    @YPBASE.setter
    def YPBASE(self, YPBASE: str):
        self.__YPBASE = YPBASE

    @property
    def XPBASE(self) -> str:
        return self.__XPBASE

    @XPBASE.setter
    def XPBASE(self, XPBASE: str):
        self.__XPBASE = XPBASE

    @property
    def YPEXTENT(self) -> str:
        return self.__YPEXTENT

    @YPEXTENT.setter
    def YPEXTENT(self, YPEXTENT: str):
        self.__YPEXTENT = YPEXTENT

class afpText_FNN(structuredField):

    def __init__(self, FNNData: str):
        self.FNNData = FNNData
        
    @property
    def FNNData(self) -> str:
        return self.__FNNData

    @FNNData.setter
    def FNNData(self, FNNData: str):
        self.__FNNData = FNNData

class afpText_EDT(structuredField):

    def __init__(self, DocName: str, afpText_EDT: set["afpText_triplet"] = None):
        self.DocName = DocName
        self.afpText_EDT = afpText_EDT if afpText_EDT is not None else set()
        
    @property
    def DocName(self) -> str:
        return self.__DocName

    @DocName.setter
    def DocName(self, DocName: str):
        self.__DocName = DocName

    @property
    def afpText_EDT(self):
        return self.__afpText_EDT

    @afpText_EDT.setter
    def afpText_EDT(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_EDT__afpText_EDT", None)
        self.__afpText_EDT = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet63"):
                    opp_val = getattr(item, "afpText_triplet63", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet63"):
                    opp_val = getattr(item, "afpText_triplet63", None)
                    
                    setattr(item, "afpText_triplet63", self)
                    

class afpText_LNC(structuredField):

    def __init__(self, NumDSC: str):
        self.NumDSC = NumDSC
        
    @property
    def NumDSC(self) -> str:
        return self.__NumDSC

    @NumDSC.setter
    def NumDSC(self, NumDSC: str):
        self.__NumDSC = NumDSC

class afpText_ERS(structuredField):

    def __init__(self, RSName: str):
        self.RSName = RSName
        
    @property
    def RSName(self) -> str:
        return self.__RSName

    @RSName.setter
    def RSName(self, RSName: str):
        self.__RSName = RSName

class afpText_FNC(structuredField):

    def __init__(self, XUnitBase: str, YUnitBase: str, XftUnits: str, YftUnits: str, MaxBoxWd: str, MaxBoxHt: str, FNORGLen: str, FNIRGLen: str, PatAlign: str, RPatDCnt: str, FNPRGLen: str, FNMRGLen: str, ResXUBase: str, ResYUBase: str, XfrUnits: str, YfrUnits: str, OPatDCnt: str, Retired: str, PatTech: str, Reserved1: str, FntFlags: str, Reserved2: str, FNNRGLen: str, FNNDCnt: str, FNNMapCnt: str, afpText_FNC: set["afpText_triplet"] = None):
        self.XUnitBase = XUnitBase
        self.YUnitBase = YUnitBase
        self.XftUnits = XftUnits
        self.YftUnits = YftUnits
        self.MaxBoxWd = MaxBoxWd
        self.MaxBoxHt = MaxBoxHt
        self.FNORGLen = FNORGLen
        self.FNIRGLen = FNIRGLen
        self.PatAlign = PatAlign
        self.RPatDCnt = RPatDCnt
        self.FNPRGLen = FNPRGLen
        self.FNMRGLen = FNMRGLen
        self.ResXUBase = ResXUBase
        self.ResYUBase = ResYUBase
        self.XfrUnits = XfrUnits
        self.YfrUnits = YfrUnits
        self.OPatDCnt = OPatDCnt
        self.Retired = Retired
        self.PatTech = PatTech
        self.Reserved1 = Reserved1
        self.FntFlags = FntFlags
        self.Reserved2 = Reserved2
        self.FNNRGLen = FNNRGLen
        self.FNNDCnt = FNNDCnt
        self.FNNMapCnt = FNNMapCnt
        self.afpText_FNC = afpText_FNC if afpText_FNC is not None else set()
        
    @property
    def FNORGLen(self) -> str:
        return self.__FNORGLen

    @FNORGLen.setter
    def FNORGLen(self, FNORGLen: str):
        self.__FNORGLen = FNORGLen

    @property
    def YftUnits(self) -> str:
        return self.__YftUnits

    @YftUnits.setter
    def YftUnits(self, YftUnits: str):
        self.__YftUnits = YftUnits

    @property
    def FNNRGLen(self) -> str:
        return self.__FNNRGLen

    @FNNRGLen.setter
    def FNNRGLen(self, FNNRGLen: str):
        self.__FNNRGLen = FNNRGLen

    @property
    def RPatDCnt(self) -> str:
        return self.__RPatDCnt

    @RPatDCnt.setter
    def RPatDCnt(self, RPatDCnt: str):
        self.__RPatDCnt = RPatDCnt

    @property
    def FNMRGLen(self) -> str:
        return self.__FNMRGLen

    @FNMRGLen.setter
    def FNMRGLen(self, FNMRGLen: str):
        self.__FNMRGLen = FNMRGLen

    @property
    def MaxBoxHt(self) -> str:
        return self.__MaxBoxHt

    @MaxBoxHt.setter
    def MaxBoxHt(self, MaxBoxHt: str):
        self.__MaxBoxHt = MaxBoxHt

    @property
    def YfrUnits(self) -> str:
        return self.__YfrUnits

    @YfrUnits.setter
    def YfrUnits(self, YfrUnits: str):
        self.__YfrUnits = YfrUnits

    @property
    def PatAlign(self) -> str:
        return self.__PatAlign

    @PatAlign.setter
    def PatAlign(self, PatAlign: str):
        self.__PatAlign = PatAlign

    @property
    def FntFlags(self) -> str:
        return self.__FntFlags

    @FntFlags.setter
    def FntFlags(self, FntFlags: str):
        self.__FntFlags = FntFlags

    @property
    def MaxBoxWd(self) -> str:
        return self.__MaxBoxWd

    @MaxBoxWd.setter
    def MaxBoxWd(self, MaxBoxWd: str):
        self.__MaxBoxWd = MaxBoxWd

    @property
    def FNIRGLen(self) -> str:
        return self.__FNIRGLen

    @FNIRGLen.setter
    def FNIRGLen(self, FNIRGLen: str):
        self.__FNIRGLen = FNIRGLen

    @property
    def FNPRGLen(self) -> str:
        return self.__FNPRGLen

    @FNPRGLen.setter
    def FNPRGLen(self, FNPRGLen: str):
        self.__FNPRGLen = FNPRGLen

    @property
    def Reserved2(self) -> str:
        return self.__Reserved2

    @Reserved2.setter
    def Reserved2(self, Reserved2: str):
        self.__Reserved2 = Reserved2

    @property
    def FNNMapCnt(self) -> str:
        return self.__FNNMapCnt

    @FNNMapCnt.setter
    def FNNMapCnt(self, FNNMapCnt: str):
        self.__FNNMapCnt = FNNMapCnt

    @property
    def XUnitBase(self) -> str:
        return self.__XUnitBase

    @XUnitBase.setter
    def XUnitBase(self, XUnitBase: str):
        self.__XUnitBase = XUnitBase

    @property
    def PatTech(self) -> str:
        return self.__PatTech

    @PatTech.setter
    def PatTech(self, PatTech: str):
        self.__PatTech = PatTech

    @property
    def ResXUBase(self) -> str:
        return self.__ResXUBase

    @ResXUBase.setter
    def ResXUBase(self, ResXUBase: str):
        self.__ResXUBase = ResXUBase

    @property
    def Retired(self) -> str:
        return self.__Retired

    @Retired.setter
    def Retired(self, Retired: str):
        self.__Retired = Retired

    @property
    def YUnitBase(self) -> str:
        return self.__YUnitBase

    @YUnitBase.setter
    def YUnitBase(self, YUnitBase: str):
        self.__YUnitBase = YUnitBase

    @property
    def OPatDCnt(self) -> str:
        return self.__OPatDCnt

    @OPatDCnt.setter
    def OPatDCnt(self, OPatDCnt: str):
        self.__OPatDCnt = OPatDCnt

    @property
    def XfrUnits(self) -> str:
        return self.__XfrUnits

    @XfrUnits.setter
    def XfrUnits(self, XfrUnits: str):
        self.__XfrUnits = XfrUnits

    @property
    def ResYUBase(self) -> str:
        return self.__ResYUBase

    @ResYUBase.setter
    def ResYUBase(self, ResYUBase: str):
        self.__ResYUBase = ResYUBase

    @property
    def Reserved1(self) -> str:
        return self.__Reserved1

    @Reserved1.setter
    def Reserved1(self, Reserved1: str):
        self.__Reserved1 = Reserved1

    @property
    def XftUnits(self) -> str:
        return self.__XftUnits

    @XftUnits.setter
    def XftUnits(self, XftUnits: str):
        self.__XftUnits = XftUnits

    @property
    def FNNDCnt(self) -> str:
        return self.__FNNDCnt

    @FNNDCnt.setter
    def FNNDCnt(self, FNNDCnt: str):
        self.__FNNDCnt = FNNDCnt

    @property
    def afpText_FNC(self):
        return self.__afpText_FNC

    @afpText_FNC.setter
    def afpText_FNC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_FNC__afpText_FNC", None)
        self.__afpText_FNC = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet83"):
                    opp_val = getattr(item, "afpText_triplet83", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet83"):
                    opp_val = getattr(item, "afpText_triplet83", None)
                    
                    setattr(item, "afpText_triplet83", self)
                    

class afpText_PEC(structuredField):

    pass
class afpText_EMM(structuredField):

    def __init__(self, MMName: str):
        self.MMName = MMName
        
    @property
    def MMName(self) -> str:
        return self.__MMName

    @MMName.setter
    def MMName(self, MMName: str):
        self.__MMName = MMName

class afpText_CDD(structuredField):

    def __init__(self, XocBase: str, YocBase: str, XocUnits: str, YocUnits: str, XocSize: str, YocSize: str, afpText_CDD: set["afpText_triplet"] = None):
        self.XocBase = XocBase
        self.YocBase = YocBase
        self.XocUnits = XocUnits
        self.YocUnits = YocUnits
        self.XocSize = XocSize
        self.YocSize = YocSize
        self.afpText_CDD = afpText_CDD if afpText_CDD is not None else set()
        
    @property
    def XocSize(self) -> str:
        return self.__XocSize

    @XocSize.setter
    def XocSize(self, XocSize: str):
        self.__XocSize = XocSize

    @property
    def XocUnits(self) -> str:
        return self.__XocUnits

    @XocUnits.setter
    def XocUnits(self, XocUnits: str):
        self.__XocUnits = XocUnits

    @property
    def YocBase(self) -> str:
        return self.__YocBase

    @YocBase.setter
    def YocBase(self, YocBase: str):
        self.__YocBase = YocBase

    @property
    def YocUnits(self) -> str:
        return self.__YocUnits

    @YocUnits.setter
    def YocUnits(self, YocUnits: str):
        self.__YocUnits = YocUnits

    @property
    def YocSize(self) -> str:
        return self.__YocSize

    @YocSize.setter
    def YocSize(self, YocSize: str):
        self.__YocSize = YocSize

    @property
    def XocBase(self) -> str:
        return self.__XocBase

    @XocBase.setter
    def XocBase(self, XocBase: str):
        self.__XocBase = XocBase

    @property
    def afpText_CDD(self):
        return self.__afpText_CDD

    @afpText_CDD.setter
    def afpText_CDD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_CDD__afpText_CDD", None)
        self.__afpText_CDD = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet51"):
                    opp_val = getattr(item, "afpText_triplet51", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet51"):
                    opp_val = getattr(item, "afpText_triplet51", None)
                    
                    setattr(item, "afpText_triplet51", self)
                    

class afpText_OBP(structuredField):

    def __init__(self, OAPosID: str, RGLength: str, XoaOset: str, YoaOset: str, XoaOrent: str, YoaOrent: str, XocaOset: str, YocaOset: str, XocaOrent: str, YocaOrent: str, RefCSys: str):
        self.OAPosID = OAPosID
        self.RGLength = RGLength
        self.XoaOset = XoaOset
        self.YoaOset = YoaOset
        self.XoaOrent = XoaOrent
        self.YoaOrent = YoaOrent
        self.XocaOset = XocaOset
        self.YocaOset = YocaOset
        self.XocaOrent = XocaOrent
        self.YocaOrent = YocaOrent
        self.RefCSys = RefCSys
        
    @property
    def YoaOset(self) -> str:
        return self.__YoaOset

    @YoaOset.setter
    def YoaOset(self, YoaOset: str):
        self.__YoaOset = YoaOset

    @property
    def XoaOrent(self) -> str:
        return self.__XoaOrent

    @XoaOrent.setter
    def XoaOrent(self, XoaOrent: str):
        self.__XoaOrent = XoaOrent

    @property
    def XocaOset(self) -> str:
        return self.__XocaOset

    @XocaOset.setter
    def XocaOset(self, XocaOset: str):
        self.__XocaOset = XocaOset

    @property
    def RGLength(self) -> str:
        return self.__RGLength

    @RGLength.setter
    def RGLength(self, RGLength: str):
        self.__RGLength = RGLength

    @property
    def YocaOrent(self) -> str:
        return self.__YocaOrent

    @YocaOrent.setter
    def YocaOrent(self, YocaOrent: str):
        self.__YocaOrent = YocaOrent

    @property
    def XocaOrent(self) -> str:
        return self.__XocaOrent

    @XocaOrent.setter
    def XocaOrent(self, XocaOrent: str):
        self.__XocaOrent = XocaOrent

    @property
    def OAPosID(self) -> str:
        return self.__OAPosID

    @OAPosID.setter
    def OAPosID(self, OAPosID: str):
        self.__OAPosID = OAPosID

    @property
    def YocaOset(self) -> str:
        return self.__YocaOset

    @YocaOset.setter
    def YocaOset(self, YocaOset: str):
        self.__YocaOset = YocaOset

    @property
    def YoaOrent(self) -> str:
        return self.__YoaOrent

    @YoaOrent.setter
    def YoaOrent(self, YoaOrent: str):
        self.__YoaOrent = YoaOrent

    @property
    def XoaOset(self) -> str:
        return self.__XoaOset

    @XoaOset.setter
    def XoaOset(self, XoaOset: str):
        self.__XoaOset = XoaOset

    @property
    def RefCSys(self) -> str:
        return self.__RefCSys

    @RefCSys.setter
    def RefCSys(self, RefCSys: str):
        self.__RefCSys = RefCSys

class afpText_BOC(structuredField):

    def __init__(self, ObjCName: str, afpText_BOC: set["afpText_triplet"] = None):
        self.ObjCName = ObjCName
        self.afpText_BOC = afpText_BOC if afpText_BOC is not None else set()
        
    @property
    def ObjCName(self) -> str:
        return self.__ObjCName

    @ObjCName.setter
    def ObjCName(self, ObjCName: str):
        self.__ObjCName = ObjCName

    @property
    def afpText_BOC(self):
        return self.__afpText_BOC

    @afpText_BOC.setter
    def afpText_BOC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_BOC__afpText_BOC", None)
        self.__afpText_BOC = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet33"):
                    opp_val = getattr(item, "afpText_triplet33", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet33"):
                    opp_val = getattr(item, "afpText_triplet33", None)
                    
                    setattr(item, "afpText_triplet33", self)
                    

class afpText_PPO(structuredField):

    pass
class afpText_BCF(structuredField):

    def __init__(self, RSName: str):
        self.RSName = RSName
        
    @property
    def RSName(self) -> str:
        return self.__RSName

    @RSName.setter
    def RSName(self, RSName: str):
        self.__RSName = RSName

class afpText_MMD(structuredField):

    pass
class afpText_MPS(structuredField):

    def __init__(self, RGLength: str, Reserved: str, afpText_MPS: set["afpText_MPSRG"] = None):
        self.RGLength = RGLength
        self.Reserved = Reserved
        self.afpText_MPS = afpText_MPS if afpText_MPS is not None else set()
        
    @property
    def RGLength(self) -> str:
        return self.__RGLength

    @RGLength.setter
    def RGLength(self, RGLength: str):
        self.__RGLength = RGLength

    @property
    def Reserved(self) -> str:
        return self.__Reserved

    @Reserved.setter
    def Reserved(self, Reserved: str):
        self.__Reserved = Reserved

    @property
    def afpText_MPS(self):
        return self.__afpText_MPS

    @afpText_MPS.setter
    def afpText_MPS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MPS__afpText_MPS", None)
        self.__afpText_MPS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_MPSRG"):
                    opp_val = getattr(item, "afpText_MPSRG", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_MPSRG", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_MPSRG"):
                    opp_val = getattr(item, "afpText_MPSRG", None)
                    
                    setattr(item, "afpText_MPSRG", self)
                    

class afpText_NOP(structuredField):

    def __init__(self, UndfData: str):
        self.UndfData = UndfData
        
    @property
    def UndfData(self) -> str:
        return self.__UndfData

    @UndfData.setter
    def UndfData(self, UndfData: str):
        self.__UndfData = UndfData

class afpText_IOB(structuredField):

    def __init__(self, XocaOset: str, YocaOset: str, RefCSys: str, ObjName: str, ObjType: str, XoaOset: str, YoaOset: str, XoaOrent: str, YoaOrent: str, afpText_IOB: set["afpText_triplet"] = None):
        self.XocaOset = XocaOset
        self.YocaOset = YocaOset
        self.RefCSys = RefCSys
        self.ObjName = ObjName
        self.ObjType = ObjType
        self.XoaOset = XoaOset
        self.YoaOset = YoaOset
        self.XoaOrent = XoaOrent
        self.YoaOrent = YoaOrent
        self.afpText_IOB = afpText_IOB if afpText_IOB is not None else set()
        
    @property
    def YocaOset(self) -> str:
        return self.__YocaOset

    @YocaOset.setter
    def YocaOset(self, YocaOset: str):
        self.__YocaOset = YocaOset

    @property
    def YoaOset(self) -> str:
        return self.__YoaOset

    @YoaOset.setter
    def YoaOset(self, YoaOset: str):
        self.__YoaOset = YoaOset

    @property
    def ObjName(self) -> str:
        return self.__ObjName

    @ObjName.setter
    def ObjName(self, ObjName: str):
        self.__ObjName = ObjName

    @property
    def XoaOrent(self) -> str:
        return self.__XoaOrent

    @XoaOrent.setter
    def XoaOrent(self, XoaOrent: str):
        self.__XoaOrent = XoaOrent

    @property
    def XoaOset(self) -> str:
        return self.__XoaOset

    @XoaOset.setter
    def XoaOset(self, XoaOset: str):
        self.__XoaOset = XoaOset

    @property
    def YoaOrent(self) -> str:
        return self.__YoaOrent

    @YoaOrent.setter
    def YoaOrent(self, YoaOrent: str):
        self.__YoaOrent = YoaOrent

    @property
    def ObjType(self) -> str:
        return self.__ObjType

    @ObjType.setter
    def ObjType(self, ObjType: str):
        self.__ObjType = ObjType

    @property
    def RefCSys(self) -> str:
        return self.__RefCSys

    @RefCSys.setter
    def RefCSys(self, RefCSys: str):
        self.__RefCSys = RefCSys

    @property
    def XocaOset(self) -> str:
        return self.__XocaOset

    @XocaOset.setter
    def XocaOset(self, XocaOset: str):
        self.__XocaOset = XocaOset

    @property
    def afpText_IOB(self):
        return self.__afpText_IOB

    @afpText_IOB.setter
    def afpText_IOB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_IOB__afpText_IOB", None)
        self.__afpText_IOB = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet99"):
                    opp_val = getattr(item, "afpText_triplet99", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet99", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet99"):
                    opp_val = getattr(item, "afpText_triplet99", None)
                    
                    setattr(item, "afpText_triplet99", self)
                    

class afpText_CFI(structuredField):

    pass
class afpText_FGD(structuredField):

    def __init__(self, ConData: str):
        self.ConData = ConData
        
    @property
    def ConData(self) -> str:
        return self.__ConData

    @ConData.setter
    def ConData(self, ConData: str):
        self.__ConData = ConData

class afpText_EFG(structuredField):

    def __init__(self, FEGName: str):
        self.FEGName = FEGName
        
    @property
    def FEGName(self) -> str:
        return self.__FEGName

    @FEGName.setter
    def FEGName(self, FEGName: str):
        self.__FEGName = FEGName

class afpText_BOG(structuredField):

    def __init__(self, OEGName: str, afpText_BOG: set["afpText_triplet"] = None):
        self.OEGName = OEGName
        self.afpText_BOG = afpText_BOG if afpText_BOG is not None else set()
        
    @property
    def OEGName(self) -> str:
        return self.__OEGName

    @OEGName.setter
    def OEGName(self, OEGName: str):
        self.__OEGName = OEGName

    @property
    def afpText_BOG(self):
        return self.__afpText_BOG

    @afpText_BOG.setter
    def afpText_BOG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_BOG__afpText_BOG", None)
        self.__afpText_BOG = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet35"):
                    opp_val = getattr(item, "afpText_triplet35", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet35"):
                    opp_val = getattr(item, "afpText_triplet35", None)
                    
                    setattr(item, "afpText_triplet35", self)
                    

class afpText_PTD(structuredField):

    def __init__(self, XPBASE: str, YPBASE: str, XPUNITVL: str, YPUNITVL: str, XPEXTENT: str, YPEXTENT: str, RESERVED: str, afpText_PTD: set["afpText_triplet"] = None):
        self.XPBASE = XPBASE
        self.YPBASE = YPBASE
        self.XPUNITVL = XPUNITVL
        self.YPUNITVL = YPUNITVL
        self.XPEXTENT = XPEXTENT
        self.YPEXTENT = YPEXTENT
        self.RESERVED = RESERVED
        self.afpText_PTD = afpText_PTD if afpText_PTD is not None else set()
        
    @property
    def XPBASE(self) -> str:
        return self.__XPBASE

    @XPBASE.setter
    def XPBASE(self, XPBASE: str):
        self.__XPBASE = XPBASE

    @property
    def YPUNITVL(self) -> str:
        return self.__YPUNITVL

    @YPUNITVL.setter
    def YPUNITVL(self, YPUNITVL: str):
        self.__YPUNITVL = YPUNITVL

    @property
    def YPBASE(self) -> str:
        return self.__YPBASE

    @YPBASE.setter
    def YPBASE(self, YPBASE: str):
        self.__YPBASE = YPBASE

    @property
    def XPEXTENT(self) -> str:
        return self.__XPEXTENT

    @XPEXTENT.setter
    def XPEXTENT(self, XPEXTENT: str):
        self.__XPEXTENT = XPEXTENT

    @property
    def XPUNITVL(self) -> str:
        return self.__XPUNITVL

    @XPUNITVL.setter
    def XPUNITVL(self, XPUNITVL: str):
        self.__XPUNITVL = XPUNITVL

    @property
    def YPEXTENT(self) -> str:
        return self.__YPEXTENT

    @YPEXTENT.setter
    def YPEXTENT(self, YPEXTENT: str):
        self.__YPEXTENT = YPEXTENT

    @property
    def RESERVED(self) -> str:
        return self.__RESERVED

    @RESERVED.setter
    def RESERVED(self, RESERVED: str):
        self.__RESERVED = RESERVED

    @property
    def afpText_PTD(self):
        return self.__afpText_PTD

    @afpText_PTD.setter
    def afpText_PTD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_PTD__afpText_PTD", None)
        self.__afpText_PTD = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet143"):
                    opp_val = getattr(item, "afpText_triplet143", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet143", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet143"):
                    opp_val = getattr(item, "afpText_triplet143", None)
                    
                    setattr(item, "afpText_triplet143", self)
                    

class afpText_MCF(structuredField):

    pass
class afpText_ESG(structuredField):

    def __init__(self, REGName: str):
        self.REGName = REGName
        
    @property
    def REGName(self) -> str:
        return self.__REGName

    @REGName.setter
    def REGName(self, REGName: str):
        self.__REGName = REGName

class afpText_BPF(structuredField):

    def __init__(self, PFName: str, afpText_BPF: set["afpText_triplet"] = None):
        self.PFName = PFName
        self.afpText_BPF = afpText_BPF if afpText_BPF is not None else set()
        
    @property
    def PFName(self) -> str:
        return self.__PFName

    @PFName.setter
    def PFName(self, PFName: str):
        self.__PFName = PFName

    @property
    def afpText_BPF(self):
        return self.__afpText_BPF

    @afpText_BPF.setter
    def afpText_BPF(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_BPF__afpText_BPF", None)
        self.__afpText_BPF = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet37"):
                    opp_val = getattr(item, "afpText_triplet37", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet37"):
                    opp_val = getattr(item, "afpText_triplet37", None)
                    
                    setattr(item, "afpText_triplet37", self)
                    

class afpText_PFC(structuredField):

    def __init__(self, PFCFlgs: str, afpText_PFC: set["afpText_triplet"] = None):
        self.PFCFlgs = PFCFlgs
        self.afpText_PFC = afpText_PFC if afpText_PFC is not None else set()
        
    @property
    def PFCFlgs(self) -> str:
        return self.__PFCFlgs

    @PFCFlgs.setter
    def PFCFlgs(self, PFCFlgs: str):
        self.__PFCFlgs = PFCFlgs

    @property
    def afpText_PFC(self):
        return self.__afpText_PFC

    @afpText_PFC.setter
    def afpText_PFC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_PFC__afpText_PFC", None)
        self.__afpText_PFC = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet135"):
                    opp_val = getattr(item, "afpText_triplet135", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet135", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet135"):
                    opp_val = getattr(item, "afpText_triplet135", None)
                    
                    setattr(item, "afpText_triplet135", self)
                    

class afpText_BMO(structuredField):

    def __init__(self, OvlyName: str, afpText_BMO: set["afpText_triplet"] = None):
        self.OvlyName = OvlyName
        self.afpText_BMO = afpText_BMO if afpText_BMO is not None else set()
        
    @property
    def OvlyName(self) -> str:
        return self.__OvlyName

    @OvlyName.setter
    def OvlyName(self, OvlyName: str):
        self.__OvlyName = OvlyName

    @property
    def afpText_BMO(self):
        return self.__afpText_BMO

    @afpText_BMO.setter
    def afpText_BMO(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_BMO__afpText_BMO", None)
        self.__afpText_BMO = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet29"):
                    opp_val = getattr(item, "afpText_triplet29", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet29"):
                    opp_val = getattr(item, "afpText_triplet29", None)
                    
                    setattr(item, "afpText_triplet29", self)
                    

class afpText_MIO(structuredField):

    pass
class afpText_BPT(structuredField):

    def __init__(self, PTdoName: str, afpText_BPT: set["afpText_triplet"] = None):
        self.PTdoName = PTdoName
        self.afpText_BPT = afpText_BPT if afpText_BPT is not None else set()
        
    @property
    def PTdoName(self) -> str:
        return self.__PTdoName

    @PTdoName.setter
    def PTdoName(self, PTdoName: str):
        self.__PTdoName = PTdoName

    @property
    def afpText_BPT(self):
        return self.__afpText_BPT

    @afpText_BPT.setter
    def afpText_BPT(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_BPT__afpText_BPT", None)
        self.__afpText_BPT = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet43"):
                    opp_val = getattr(item, "afpText_triplet43", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet43"):
                    opp_val = getattr(item, "afpText_triplet43", None)
                    
                    setattr(item, "afpText_triplet43", self)
                    

class afpText_IPO(structuredField):

    def __init__(self, OvlyName: str, XolOset: str, YolOset: str, OvlyOrent: str, afpText_IPO: set["afpText_triplet"] = None):
        self.OvlyName = OvlyName
        self.XolOset = XolOset
        self.YolOset = YolOset
        self.OvlyOrent = OvlyOrent
        self.afpText_IPO = afpText_IPO if afpText_IPO is not None else set()
        
    @property
    def OvlyName(self) -> str:
        return self.__OvlyName

    @OvlyName.setter
    def OvlyName(self, OvlyName: str):
        self.__OvlyName = OvlyName

    @property
    def OvlyOrent(self) -> str:
        return self.__OvlyOrent

    @OvlyOrent.setter
    def OvlyOrent(self, OvlyOrent: str):
        self.__OvlyOrent = OvlyOrent

    @property
    def XolOset(self) -> str:
        return self.__XolOset

    @XolOset.setter
    def XolOset(self, XolOset: str):
        self.__XolOset = XolOset

    @property
    def YolOset(self) -> str:
        return self.__YolOset

    @YolOset.setter
    def YolOset(self, YolOset: str):
        self.__YolOset = YolOset

    @property
    def afpText_IPO(self):
        return self.__afpText_IPO

    @afpText_IPO.setter
    def afpText_IPO(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_IPO__afpText_IPO", None)
        self.__afpText_IPO = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet103"):
                    opp_val = getattr(item, "afpText_triplet103", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet103"):
                    opp_val = getattr(item, "afpText_triplet103", None)
                    
                    setattr(item, "afpText_triplet103", self)
                    

class afpText_CPC(structuredField):

    def __init__(self, DefCharID: str, PrtFlags: str, CPIRGLen: str, VSCharSN: str, VSChar: str, VSFlags: str):
        self.DefCharID = DefCharID
        self.PrtFlags = PrtFlags
        self.CPIRGLen = CPIRGLen
        self.VSCharSN = VSCharSN
        self.VSChar = VSChar
        self.VSFlags = VSFlags
        
    @property
    def VSCharSN(self) -> str:
        return self.__VSCharSN

    @VSCharSN.setter
    def VSCharSN(self, VSCharSN: str):
        self.__VSCharSN = VSCharSN

    @property
    def DefCharID(self) -> str:
        return self.__DefCharID

    @DefCharID.setter
    def DefCharID(self, DefCharID: str):
        self.__DefCharID = DefCharID

    @property
    def CPIRGLen(self) -> str:
        return self.__CPIRGLen

    @CPIRGLen.setter
    def CPIRGLen(self, CPIRGLen: str):
        self.__CPIRGLen = CPIRGLen

    @property
    def PrtFlags(self) -> str:
        return self.__PrtFlags

    @PrtFlags.setter
    def PrtFlags(self, PrtFlags: str):
        self.__PrtFlags = PrtFlags

    @property
    def VSChar(self) -> str:
        return self.__VSChar

    @VSChar.setter
    def VSChar(self, VSChar: str):
        self.__VSChar = VSChar

    @property
    def VSFlags(self) -> str:
        return self.__VSFlags

    @VSFlags.setter
    def VSFlags(self, VSFlags: str):
        self.__VSFlags = VSFlags

class afpText_BII(structuredField):

    def __init__(self, ImoName: str):
        self.ImoName = ImoName
        
    @property
    def ImoName(self) -> str:
        return self.__ImoName

    @ImoName.setter
    def ImoName(self, ImoName: str):
        self.__ImoName = ImoName

class afpText_FNO(structuredField):

    pass
class afpText_BRG(structuredField):

    def __init__(self, RGrpName: str, afpText_BRG: set["afpText_triplet"] = None):
        self.RGrpName = RGrpName
        self.afpText_BRG = afpText_BRG if afpText_BRG is not None else set()
        
    @property
    def RGrpName(self) -> str:
        return self.__RGrpName

    @RGrpName.setter
    def RGrpName(self, RGrpName: str):
        self.__RGrpName = RGrpName

    @property
    def afpText_BRG(self):
        return self.__afpText_BRG

    @afpText_BRG.setter
    def afpText_BRG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_BRG__afpText_BRG", None)
        self.__afpText_BRG = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet45"):
                    opp_val = getattr(item, "afpText_triplet45", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet45"):
                    opp_val = getattr(item, "afpText_triplet45", None)
                    
                    setattr(item, "afpText_triplet45", self)
                    

class afpText_PGP1(structuredField):

    def __init__(self, XOset: str, YOset: str):
        self.XOset = XOset
        self.YOset = YOset
        
    @property
    def YOset(self) -> str:
        return self.__YOset

    @YOset.setter
    def YOset(self, YOset: str):
        self.__YOset = YOset

    @property
    def XOset(self) -> str:
        return self.__XOset

    @XOset.setter
    def XOset(self, XOset: str):
        self.__XOset = XOset

class afpText_BPS(structuredField):

    def __init__(self, PsegName: str, afpText_BPS: set["afpText_triplet"] = None):
        self.PsegName = PsegName
        self.afpText_BPS = afpText_BPS if afpText_BPS is not None else set()
        
    @property
    def PsegName(self) -> str:
        return self.__PsegName

    @PsegName.setter
    def PsegName(self, PsegName: str):
        self.__PsegName = PsegName

    @property
    def afpText_BPS(self):
        return self.__afpText_BPS

    @afpText_BPS.setter
    def afpText_BPS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_BPS__afpText_BPS", None)
        self.__afpText_BPS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet41"):
                    opp_val = getattr(item, "afpText_triplet41", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet41"):
                    opp_val = getattr(item, "afpText_triplet41", None)
                    
                    setattr(item, "afpText_triplet41", self)
                    

class afpText_CFC(structuredField):

    def __init__(self, CFIRGLen: str, Retired1: str, afpText_CFC: set["afpText_triplet"] = None):
        self.CFIRGLen = CFIRGLen
        self.Retired1 = Retired1
        self.afpText_CFC = afpText_CFC if afpText_CFC is not None else set()
        
    @property
    def Retired1(self) -> str:
        return self.__Retired1

    @Retired1.setter
    def Retired1(self, Retired1: str):
        self.__Retired1 = Retired1

    @property
    def CFIRGLen(self) -> str:
        return self.__CFIRGLen

    @CFIRGLen.setter
    def CFIRGLen(self, CFIRGLen: str):
        self.__CFIRGLen = CFIRGLen

    @property
    def afpText_CFC(self):
        return self.__afpText_CFC

    @afpText_CFC.setter
    def afpText_CFC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_CFC__afpText_CFC", None)
        self.__afpText_CFC = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet53"):
                    opp_val = getattr(item, "afpText_triplet53", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet53"):
                    opp_val = getattr(item, "afpText_triplet53", None)
                    
                    setattr(item, "afpText_triplet53", self)
                    

class afpText_MPG(structuredField):

    pass
class afpText_BIM(structuredField):

    def __init__(self, IdoName: str, afpText_BIM: set["afpText_triplet"] = None):
        self.IdoName = IdoName
        self.afpText_BIM = afpText_BIM if afpText_BIM is not None else set()
        
    @property
    def IdoName(self) -> str:
        return self.__IdoName

    @IdoName.setter
    def IdoName(self, IdoName: str):
        self.__IdoName = IdoName

    @property
    def afpText_BIM(self):
        return self.__afpText_BIM

    @afpText_BIM.setter
    def afpText_BIM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_BIM__afpText_BIM", None)
        self.__afpText_BIM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet25"):
                    opp_val = getattr(item, "afpText_triplet25", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet25"):
                    opp_val = getattr(item, "afpText_triplet25", None)
                    
                    setattr(item, "afpText_triplet25", self)
                    

class afpText_EDM(structuredField):

    def __init__(self, DMName: str):
        self.DMName = DMName
        
    @property
    def DMName(self) -> str:
        return self.__DMName

    @DMName.setter
    def DMName(self, DMName: str):
        self.__DMName = DMName

class afpText_MDD(structuredField):

    def __init__(self, XmBase: str, YmBase: str, XmUnits: str, YmUnits: str, XmSize: str, YmSize: str, MDDFlgs: str, afpText_MDD: set["afpText_triplet"] = None):
        self.XmBase = XmBase
        self.YmBase = YmBase
        self.XmUnits = XmUnits
        self.YmUnits = YmUnits
        self.XmSize = XmSize
        self.YmSize = YmSize
        self.MDDFlgs = MDDFlgs
        self.afpText_MDD = afpText_MDD if afpText_MDD is not None else set()
        
    @property
    def YmBase(self) -> str:
        return self.__YmBase

    @YmBase.setter
    def YmBase(self, YmBase: str):
        self.__YmBase = YmBase

    @property
    def YmUnits(self) -> str:
        return self.__YmUnits

    @YmUnits.setter
    def YmUnits(self, YmUnits: str):
        self.__YmUnits = YmUnits

    @property
    def XmBase(self) -> str:
        return self.__XmBase

    @XmBase.setter
    def XmBase(self, XmBase: str):
        self.__XmBase = XmBase

    @property
    def XmSize(self) -> str:
        return self.__XmSize

    @XmSize.setter
    def XmSize(self, XmSize: str):
        self.__XmSize = XmSize

    @property
    def XmUnits(self) -> str:
        return self.__XmUnits

    @XmUnits.setter
    def XmUnits(self, XmUnits: str):
        self.__XmUnits = XmUnits

    @property
    def YmSize(self) -> str:
        return self.__YmSize

    @YmSize.setter
    def YmSize(self, YmSize: str):
        self.__YmSize = YmSize

    @property
    def MDDFlgs(self) -> str:
        return self.__MDDFlgs

    @MDDFlgs.setter
    def MDDFlgs(self, MDDFlgs: str):
        self.__MDDFlgs = MDDFlgs

    @property
    def afpText_MDD(self):
        return self.__afpText_MDD

    @afpText_MDD.setter
    def afpText_MDD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MDD__afpText_MDD", None)
        self.__afpText_MDD = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet116"):
                    opp_val = getattr(item, "afpText_triplet116", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet116"):
                    opp_val = getattr(item, "afpText_triplet116", None)
                    
                    setattr(item, "afpText_triplet116", self)
                    

class afpText_FNP(structuredField):

    pass
class afpText_FNG(structuredField):

    def __init__(self, PatData: str):
        self.PatData = PatData
        
    @property
    def PatData(self) -> str:
        return self.__PatData

    @PatData.setter
    def PatData(self, PatData: str):
        self.__PatData = PatData

class afpText_MMT(structuredField):

    pass
class afpText_EAG(structuredField):

    def __init__(self, AEGName: str):
        self.AEGName = AEGName
        
    @property
    def AEGName(self) -> str:
        return self.__AEGName

    @AEGName.setter
    def AEGName(self, AEGName: str):
        self.__AEGName = AEGName

class afpText_BMM(structuredField):

    def __init__(self, MMName: str, afpText_BMM: set["afpText_triplet"] = None):
        self.MMName = MMName
        self.afpText_BMM = afpText_BMM if afpText_BMM is not None else set()
        
    @property
    def MMName(self) -> str:
        return self.__MMName

    @MMName.setter
    def MMName(self, MMName: str):
        self.__MMName = MMName

    @property
    def afpText_BMM(self):
        return self.__afpText_BMM

    @afpText_BMM.setter
    def afpText_BMM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_BMM__afpText_BMM", None)
        self.__afpText_BMM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet27"):
                    opp_val = getattr(item, "afpText_triplet27", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet27"):
                    opp_val = getattr(item, "afpText_triplet27", None)
                    
                    setattr(item, "afpText_triplet27", self)
                    

class afpText_MCF1(structuredField):

    def __init__(self, RGLength: str, afpText_MCF1: set["afpText_MCF1RG"] = None):
        self.RGLength = RGLength
        self.afpText_MCF1 = afpText_MCF1 if afpText_MCF1 is not None else set()
        
    @property
    def RGLength(self) -> str:
        return self.__RGLength

    @RGLength.setter
    def RGLength(self, RGLength: str):
        self.__RGLength = RGLength

    @property
    def afpText_MCF1(self):
        return self.__afpText_MCF1

    @afpText_MCF1.setter
    def afpText_MCF1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MCF1__afpText_MCF1", None)
        self.__afpText_MCF1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_MCF1RG"):
                    opp_val = getattr(item, "afpText_MCF1RG", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_MCF1RG", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_MCF1RG"):
                    opp_val = getattr(item, "afpText_MCF1RG", None)
                    
                    setattr(item, "afpText_MCF1RG", self)
                    

class afpText_BGR(structuredField):

    def __init__(self, GdoName: str, afpText_BGR: set["afpText_triplet"] = None):
        self.GdoName = GdoName
        self.afpText_BGR = afpText_BGR if afpText_BGR is not None else set()
        
    @property
    def GdoName(self) -> str:
        return self.__GdoName

    @GdoName.setter
    def GdoName(self, GdoName: str):
        self.__GdoName = GdoName

    @property
    def afpText_BGR(self):
        return self.__afpText_BGR

    @afpText_BGR.setter
    def afpText_BGR(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_BGR__afpText_BGR", None)
        self.__afpText_BGR = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet23"):
                    opp_val = getattr(item, "afpText_triplet23", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet23"):
                    opp_val = getattr(item, "afpText_triplet23", None)
                    
                    setattr(item, "afpText_triplet23", self)
                    

class afpText_ICP(structuredField):

    def __init__(self, XCOset: str, YCOset: str, XCSize: str, YCSize: str, XFilSize: str, YFilSize: str):
        self.XCOset = XCOset
        self.YCOset = YCOset
        self.XCSize = XCSize
        self.YCSize = YCSize
        self.XFilSize = XFilSize
        self.YFilSize = YFilSize
        
    @property
    def YCOset(self) -> str:
        return self.__YCOset

    @YCOset.setter
    def YCOset(self, YCOset: str):
        self.__YCOset = YCOset

    @property
    def YCSize(self) -> str:
        return self.__YCSize

    @YCSize.setter
    def YCSize(self, YCSize: str):
        self.__YCSize = YCSize

    @property
    def XCOset(self) -> str:
        return self.__XCOset

    @XCOset.setter
    def XCOset(self, XCOset: str):
        self.__XCOset = XCOset

    @property
    def XCSize(self) -> str:
        return self.__XCSize

    @XCSize.setter
    def XCSize(self, XCSize: str):
        self.__XCSize = XCSize

    @property
    def YFilSize(self) -> str:
        return self.__YFilSize

    @YFilSize.setter
    def YFilSize(self, YFilSize: str):
        self.__YFilSize = YFilSize

    @property
    def XFilSize(self) -> str:
        return self.__XFilSize

    @XFilSize.setter
    def XFilSize(self, XFilSize: str):
        self.__XFilSize = XFilSize

class afpText_ECA(structuredField):

    def __init__(self, CATName: str, afpText_ECA: set["afpText_triplet"] = None):
        self.CATName = CATName
        self.afpText_ECA = afpText_ECA if afpText_ECA is not None else set()
        
    @property
    def CATName(self) -> str:
        return self.__CATName

    @CATName.setter
    def CATName(self, CATName: str):
        self.__CATName = CATName

    @property
    def afpText_ECA(self):
        return self.__afpText_ECA

    @afpText_ECA.setter
    def afpText_ECA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_ECA__afpText_ECA", None)
        self.__afpText_ECA = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet59"):
                    opp_val = getattr(item, "afpText_triplet59", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet59"):
                    opp_val = getattr(item, "afpText_triplet59", None)
                    
                    setattr(item, "afpText_triplet59", self)
                    

class afpText_BDA(structuredField):

    def __init__(self, Yoffset: str, Data: str, Flags: str, Xoffset: str):
        self.Yoffset = Yoffset
        self.Data = Data
        self.Flags = Flags
        self.Xoffset = Xoffset
        
    @property
    def Data(self) -> str:
        return self.__Data

    @Data.setter
    def Data(self, Data: str):
        self.__Data = Data

    @property
    def Yoffset(self) -> str:
        return self.__Yoffset

    @Yoffset.setter
    def Yoffset(self, Yoffset: str):
        self.__Yoffset = Yoffset

    @property
    def Flags(self) -> str:
        return self.__Flags

    @Flags.setter
    def Flags(self, Flags: str):
        self.__Flags = Flags

    @property
    def Xoffset(self) -> str:
        return self.__Xoffset

    @Xoffset.setter
    def Xoffset(self, Xoffset: str):
        self.__Xoffset = Xoffset

class afpText_IDD(structuredField):

    def __init__(self, UNITBASE: str, XRESOL: str, YRESOL: str, XSIZE: str, YSIZE: str, afpText_IDD: set["afpText_triplet"] = None):
        self.UNITBASE = UNITBASE
        self.XRESOL = XRESOL
        self.YRESOL = YRESOL
        self.XSIZE = XSIZE
        self.YSIZE = YSIZE
        self.afpText_IDD = afpText_IDD if afpText_IDD is not None else set()
        
    @property
    def UNITBASE(self) -> str:
        return self.__UNITBASE

    @UNITBASE.setter
    def UNITBASE(self, UNITBASE: str):
        self.__UNITBASE = UNITBASE

    @property
    def YRESOL(self) -> str:
        return self.__YRESOL

    @YRESOL.setter
    def YRESOL(self, YRESOL: str):
        self.__YRESOL = YRESOL

    @property
    def XSIZE(self) -> str:
        return self.__XSIZE

    @XSIZE.setter
    def XSIZE(self, XSIZE: str):
        self.__XSIZE = XSIZE

    @property
    def XRESOL(self) -> str:
        return self.__XRESOL

    @XRESOL.setter
    def XRESOL(self, XRESOL: str):
        self.__XRESOL = XRESOL

    @property
    def YSIZE(self) -> str:
        return self.__YSIZE

    @YSIZE.setter
    def YSIZE(self, YSIZE: str):
        self.__YSIZE = YSIZE

    @property
    def afpText_IDD(self):
        return self.__afpText_IDD

    @afpText_IDD.setter
    def afpText_IDD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_IDD__afpText_IDD", None)
        self.__afpText_IDD = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet93"):
                    opp_val = getattr(item, "afpText_triplet93", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet93"):
                    opp_val = getattr(item, "afpText_triplet93", None)
                    
                    setattr(item, "afpText_triplet93", self)
                    

class afpText_ERG(structuredField):

    def __init__(self, RGrpName: str, afpText_ERG: set["afpText_triplet"] = None):
        self.RGrpName = RGrpName
        self.afpText_ERG = afpText_ERG if afpText_ERG is not None else set()
        
    @property
    def RGrpName(self) -> str:
        return self.__RGrpName

    @RGrpName.setter
    def RGrpName(self, RGrpName: str):
        self.__RGrpName = RGrpName

    @property
    def afpText_ERG(self):
        return self.__afpText_ERG

    @afpText_ERG.setter
    def afpText_ERG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_ERG__afpText_ERG", None)
        self.__afpText_ERG = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet81"):
                    opp_val = getattr(item, "afpText_triplet81", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet81"):
                    opp_val = getattr(item, "afpText_triplet81", None)
                    
                    setattr(item, "afpText_triplet81", self)
                    

class afpText_EPF(structuredField):

    def __init__(self, PFName: str, afpText_EPF: set["afpText_triplet"] = None):
        self.PFName = PFName
        self.afpText_EPF = afpText_EPF if afpText_EPF is not None else set()
        
    @property
    def PFName(self) -> str:
        return self.__PFName

    @PFName.setter
    def PFName(self, PFName: str):
        self.__PFName = PFName

    @property
    def afpText_EPF(self):
        return self.__afpText_EPF

    @afpText_EPF.setter
    def afpText_EPF(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_EPF__afpText_EPF", None)
        self.__afpText_EPF = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet75"):
                    opp_val = getattr(item, "afpText_triplet75", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet75"):
                    opp_val = getattr(item, "afpText_triplet75", None)
                    
                    setattr(item, "afpText_triplet75", self)
                    

class afpText_ECP(structuredField):

    def __init__(self, RSName: str):
        self.RSName = RSName
        
    @property
    def RSName(self) -> str:
        return self.__RSName

    @RSName.setter
    def RSName(self, RSName: str):
        self.__RSName = RSName

class afpText_MCC(structuredField):

    pass
class afpText_BDX(structuredField):

    def __init__(self, DMXName: str):
        self.DMXName = DMXName
        
    @property
    def DMXName(self) -> str:
        return self.__DMXName

    @DMXName.setter
    def DMXName(self, DMXName: str):
        self.__DMXName = DMXName

class afpText_CPD(structuredField):

    def __init__(self, CPDesc: str, GCGIDLen: str, NumCdPts: str, GCSGID: str, CPGID: str, EncScheme: str):
        self.CPDesc = CPDesc
        self.GCGIDLen = GCGIDLen
        self.NumCdPts = NumCdPts
        self.GCSGID = GCSGID
        self.CPGID = CPGID
        self.EncScheme = EncScheme
        
    @property
    def GCSGID(self) -> str:
        return self.__GCSGID

    @GCSGID.setter
    def GCSGID(self, GCSGID: str):
        self.__GCSGID = GCSGID

    @property
    def GCGIDLen(self) -> str:
        return self.__GCGIDLen

    @GCGIDLen.setter
    def GCGIDLen(self, GCGIDLen: str):
        self.__GCGIDLen = GCGIDLen

    @property
    def CPGID(self) -> str:
        return self.__CPGID

    @CPGID.setter
    def CPGID(self, CPGID: str):
        self.__CPGID = CPGID

    @property
    def EncScheme(self) -> str:
        return self.__EncScheme

    @EncScheme.setter
    def EncScheme(self, EncScheme: str):
        self.__EncScheme = EncScheme

    @property
    def CPDesc(self) -> str:
        return self.__CPDesc

    @CPDesc.setter
    def CPDesc(self, CPDesc: str):
        self.__CPDesc = CPDesc

    @property
    def NumCdPts(self) -> str:
        return self.__NumCdPts

    @NumCdPts.setter
    def NumCdPts(self, NumCdPts: str):
        self.__NumCdPts = NumCdPts

class afpText_EII(structuredField):

    def __init__(self, ImoName: str):
        self.ImoName = ImoName
        
    @property
    def ImoName(self) -> str:
        return self.__ImoName

    @ImoName.setter
    def ImoName(self, ImoName: str):
        self.__ImoName = ImoName

class afpText_BDM(structuredField):

    def __init__(self, DMName: str, DatFmt: str, afpText_BDM: set["afpText_triplet"] = None):
        self.DMName = DMName
        self.DatFmt = DatFmt
        self.afpText_BDM = afpText_BDM if afpText_BDM is not None else set()
        
    @property
    def DMName(self) -> str:
        return self.__DMName

    @DMName.setter
    def DMName(self, DMName: str):
        self.__DMName = DMName

    @property
    def DatFmt(self) -> str:
        return self.__DatFmt

    @DatFmt.setter
    def DatFmt(self, DatFmt: str):
        self.__DatFmt = DatFmt

    @property
    def afpText_BDM(self):
        return self.__afpText_BDM

    @afpText_BDM.setter
    def afpText_BDM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_BDM__afpText_BDM", None)
        self.__afpText_BDM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet15"):
                    opp_val = getattr(item, "afpText_triplet15", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet15"):
                    opp_val = getattr(item, "afpText_triplet15", None)
                    
                    setattr(item, "afpText_triplet15", self)
                    

class afpText_MPO(structuredField):

    pass
class afpText_EGR(structuredField):

    def __init__(self, GdoName: str, afpText_EGR: set["afpText_triplet"] = None):
        self.GdoName = GdoName
        self.afpText_EGR = afpText_EGR if afpText_EGR is not None else set()
        
    @property
    def GdoName(self) -> str:
        return self.__GdoName

    @GdoName.setter
    def GdoName(self, GdoName: str):
        self.__GdoName = GdoName

    @property
    def afpText_EGR(self):
        return self.__afpText_EGR

    @afpText_EGR.setter
    def afpText_EGR(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_EGR__afpText_EGR", None)
        self.__afpText_EGR = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet65"):
                    opp_val = getattr(item, "afpText_triplet65", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet65"):
                    opp_val = getattr(item, "afpText_triplet65", None)
                    
                    setattr(item, "afpText_triplet65", self)
                    

class afpText_BFG(structuredField):

    def __init__(self, FEGName: str):
        self.FEGName = FEGName
        
    @property
    def FEGName(self) -> str:
        return self.__FEGName

    @FEGName.setter
    def FEGName(self, FEGName: str):
        self.__FEGName = FEGName

class afpText_BRS(structuredField):

    def __init__(self, RSName: str, afpText_BRS: set["afpText_triplet"] = None):
        self.RSName = RSName
        self.afpText_BRS = afpText_BRS if afpText_BRS is not None else set()
        
    @property
    def RSName(self) -> str:
        return self.__RSName

    @RSName.setter
    def RSName(self, RSName: str):
        self.__RSName = RSName

    @property
    def afpText_BRS(self):
        return self.__afpText_BRS

    @afpText_BRS.setter
    def afpText_BRS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_BRS__afpText_BRS", None)
        self.__afpText_BRS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet47"):
                    opp_val = getattr(item, "afpText_triplet47", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet47"):
                    opp_val = getattr(item, "afpText_triplet47", None)
                    
                    setattr(item, "afpText_triplet47", self)
                    

class afpText_BNG(structuredField):

    def __init__(self, PGrpName: str, afpText_BNG: set["afpText_triplet"] = None):
        self.PGrpName = PGrpName
        self.afpText_BNG = afpText_BNG if afpText_BNG is not None else set()
        
    @property
    def PGrpName(self) -> str:
        return self.__PGrpName

    @PGrpName.setter
    def PGrpName(self, PGrpName: str):
        self.__PGrpName = PGrpName

    @property
    def afpText_BNG(self):
        return self.__afpText_BNG

    @afpText_BNG.setter
    def afpText_BNG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_BNG__afpText_BNG", None)
        self.__afpText_BNG = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet31"):
                    opp_val = getattr(item, "afpText_triplet31", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet31"):
                    opp_val = getattr(item, "afpText_triplet31", None)
                    
                    setattr(item, "afpText_triplet31", self)
                    

class afpText_FNM(structuredField):

    pass
class afpText_EOG(structuredField):

    def __init__(self, OEGName: str):
        self.OEGName = OEGName
        
    @property
    def OEGName(self) -> str:
        return self.__OEGName

    @OEGName.setter
    def OEGName(self, OEGName: str):
        self.__OEGName = OEGName

class afpText_TLE(structuredField):

    pass
class afpText_BPG(structuredField):

    def __init__(self, PageName: str, afpText_BPG: set["afpText_triplet"] = None):
        self.PageName = PageName
        self.afpText_BPG = afpText_BPG if afpText_BPG is not None else set()
        
    @property
    def PageName(self) -> str:
        return self.__PageName

    @PageName.setter
    def PageName(self, PageName: str):
        self.__PageName = PageName

    @property
    def afpText_BPG(self):
        return self.__afpText_BPG

    @afpText_BPG.setter
    def afpText_BPG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_BPG__afpText_BPG", None)
        self.__afpText_BPG = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet39"):
                    opp_val = getattr(item, "afpText_triplet39", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet39"):
                    opp_val = getattr(item, "afpText_triplet39", None)
                    
                    setattr(item, "afpText_triplet39", self)
                    

class afpText_IRD(structuredField):

    def __init__(self, IMdata: str):
        self.IMdata = IMdata
        
    @property
    def IMdata(self) -> str:
        return self.__IMdata

    @IMdata.setter
    def IMdata(self, IMdata: str):
        self.__IMdata = IMdata

class afpText_ECF(structuredField):

    def __init__(self, RSName: str):
        self.RSName = RSName
        
    @property
    def RSName(self) -> str:
        return self.__RSName

    @RSName.setter
    def RSName(self, RSName: str):
        self.__RSName = RSName

class afpText_DXD(structuredField):

    pass
class afpText_MCA(structuredField):

    pass
class afpText_MSU(structuredField):

    pass
class afpText_PMC(structuredField):

    def __init__(self, PMCid: str, afpText_PMC: set["afpText_triplet"] = None):
        self.PMCid = PMCid
        self.afpText_PMC = afpText_PMC if afpText_PMC is not None else set()
        
    @property
    def PMCid(self) -> str:
        return self.__PMCid

    @PMCid.setter
    def PMCid(self, PMCid: str):
        self.__PMCid = PMCid

    @property
    def afpText_PMC(self):
        return self.__afpText_PMC

    @afpText_PMC.setter
    def afpText_PMC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_PMC__afpText_PMC", None)
        self.__afpText_PMC = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet140"):
                    opp_val = getattr(item, "afpText_triplet140", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet140", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet140"):
                    opp_val = getattr(item, "afpText_triplet140", None)
                    
                    setattr(item, "afpText_triplet140", self)
                    

class afpText_OBD(structuredField):

    pass
class afpText_BFM(structuredField):

    def __init__(self, FMName: str, afpText_BFM: set["afpText_triplet"] = None):
        self.FMName = FMName
        self.afpText_BFM = afpText_BFM if afpText_BFM is not None else set()
        
    @property
    def FMName(self) -> str:
        return self.__FMName

    @FMName.setter
    def FMName(self, FMName: str):
        self.__FMName = FMName

    @property
    def afpText_BFM(self):
        return self.__afpText_BFM

    @afpText_BFM.setter
    def afpText_BFM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_BFM__afpText_BFM", None)
        self.__afpText_BFM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet19"):
                    opp_val = getattr(item, "afpText_triplet19", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet19"):
                    opp_val = getattr(item, "afpText_triplet19", None)
                    
                    setattr(item, "afpText_triplet19", self)
                    

class afpText_IMM(structuredField):

    def __init__(self, MMPName: str, afpText_IMM: set["afpText_triplet"] = None):
        self.MMPName = MMPName
        self.afpText_IMM = afpText_IMM if afpText_IMM is not None else set()
        
    @property
    def MMPName(self) -> str:
        return self.__MMPName

    @MMPName.setter
    def MMPName(self, MMPName: str):
        self.__MMPName = MMPName

    @property
    def afpText_IMM(self):
        return self.__afpText_IMM

    @afpText_IMM.setter
    def afpText_IMM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_IMM__afpText_IMM", None)
        self.__afpText_IMM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet97"):
                    opp_val = getattr(item, "afpText_triplet97", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet97", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet97"):
                    opp_val = getattr(item, "afpText_triplet97", None)
                    
                    setattr(item, "afpText_triplet97", self)
                    

class afpText_CTC(structuredField):

    def __init__(self, ConData: str):
        self.ConData = ConData
        
    @property
    def ConData(self) -> str:
        return self.__ConData

    @ConData.setter
    def ConData(self, ConData: str):
        self.__ConData = ConData

class afpText_BFN(structuredField):

    def __init__(self, RSName: str, afpText_BFN: set["afpText_triplet"] = None):
        self.RSName = RSName
        self.afpText_BFN = afpText_BFN if afpText_BFN is not None else set()
        
    @property
    def RSName(self) -> str:
        return self.__RSName

    @RSName.setter
    def RSName(self, RSName: str):
        self.__RSName = RSName

    @property
    def afpText_BFN(self):
        return self.__afpText_BFN

    @afpText_BFN.setter
    def afpText_BFN(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_BFN__afpText_BFN", None)
        self.__afpText_BFN = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet21"):
                    opp_val = getattr(item, "afpText_triplet21", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet21"):
                    opp_val = getattr(item, "afpText_triplet21", None)
                    
                    setattr(item, "afpText_triplet21", self)
                    

class afpText_FND(structuredField):

    def __init__(self, TypeFcDesc: str, FtWtClass: str, FtWdClass: str, MaxPtSize: str, NomPtSize: str, MinPtSize: str, MaxHSize: str, NomHSize: str, MinHSize: str, DsnGenCls: str, DsnSubCls: str, DsnSpcGrp: str, Reserved1: str, FtDsFlags: str, Reserved2: str, GCSID: str, FGID: str, afpText_FND: set["afpText_triplet"] = None):
        self.TypeFcDesc = TypeFcDesc
        self.FtWtClass = FtWtClass
        self.FtWdClass = FtWdClass
        self.MaxPtSize = MaxPtSize
        self.NomPtSize = NomPtSize
        self.MinPtSize = MinPtSize
        self.MaxHSize = MaxHSize
        self.NomHSize = NomHSize
        self.MinHSize = MinHSize
        self.DsnGenCls = DsnGenCls
        self.DsnSubCls = DsnSubCls
        self.DsnSpcGrp = DsnSpcGrp
        self.Reserved1 = Reserved1
        self.FtDsFlags = FtDsFlags
        self.Reserved2 = Reserved2
        self.GCSID = GCSID
        self.FGID = FGID
        self.afpText_FND = afpText_FND if afpText_FND is not None else set()
        
    @property
    def Reserved2(self) -> str:
        return self.__Reserved2

    @Reserved2.setter
    def Reserved2(self, Reserved2: str):
        self.__Reserved2 = Reserved2

    @property
    def MaxHSize(self) -> str:
        return self.__MaxHSize

    @MaxHSize.setter
    def MaxHSize(self, MaxHSize: str):
        self.__MaxHSize = MaxHSize

    @property
    def FtWtClass(self) -> str:
        return self.__FtWtClass

    @FtWtClass.setter
    def FtWtClass(self, FtWtClass: str):
        self.__FtWtClass = FtWtClass

    @property
    def NomHSize(self) -> str:
        return self.__NomHSize

    @NomHSize.setter
    def NomHSize(self, NomHSize: str):
        self.__NomHSize = NomHSize

    @property
    def NomPtSize(self) -> str:
        return self.__NomPtSize

    @NomPtSize.setter
    def NomPtSize(self, NomPtSize: str):
        self.__NomPtSize = NomPtSize

    @property
    def FGID(self) -> str:
        return self.__FGID

    @FGID.setter
    def FGID(self, FGID: str):
        self.__FGID = FGID

    @property
    def MaxPtSize(self) -> str:
        return self.__MaxPtSize

    @MaxPtSize.setter
    def MaxPtSize(self, MaxPtSize: str):
        self.__MaxPtSize = MaxPtSize

    @property
    def DsnSubCls(self) -> str:
        return self.__DsnSubCls

    @DsnSubCls.setter
    def DsnSubCls(self, DsnSubCls: str):
        self.__DsnSubCls = DsnSubCls

    @property
    def DsnSpcGrp(self) -> str:
        return self.__DsnSpcGrp

    @DsnSpcGrp.setter
    def DsnSpcGrp(self, DsnSpcGrp: str):
        self.__DsnSpcGrp = DsnSpcGrp

    @property
    def MinPtSize(self) -> str:
        return self.__MinPtSize

    @MinPtSize.setter
    def MinPtSize(self, MinPtSize: str):
        self.__MinPtSize = MinPtSize

    @property
    def Reserved1(self) -> str:
        return self.__Reserved1

    @Reserved1.setter
    def Reserved1(self, Reserved1: str):
        self.__Reserved1 = Reserved1

    @property
    def MinHSize(self) -> str:
        return self.__MinHSize

    @MinHSize.setter
    def MinHSize(self, MinHSize: str):
        self.__MinHSize = MinHSize

    @property
    def TypeFcDesc(self) -> str:
        return self.__TypeFcDesc

    @TypeFcDesc.setter
    def TypeFcDesc(self, TypeFcDesc: str):
        self.__TypeFcDesc = TypeFcDesc

    @property
    def FtDsFlags(self) -> str:
        return self.__FtDsFlags

    @FtDsFlags.setter
    def FtDsFlags(self, FtDsFlags: str):
        self.__FtDsFlags = FtDsFlags

    @property
    def DsnGenCls(self) -> str:
        return self.__DsnGenCls

    @DsnGenCls.setter
    def DsnGenCls(self, DsnGenCls: str):
        self.__DsnGenCls = DsnGenCls

    @property
    def FtWdClass(self) -> str:
        return self.__FtWdClass

    @FtWdClass.setter
    def FtWdClass(self, FtWdClass: str):
        self.__FtWdClass = FtWdClass

    @property
    def GCSID(self) -> str:
        return self.__GCSID

    @GCSID.setter
    def GCSID(self, GCSID: str):
        self.__GCSID = GCSID

    @property
    def afpText_FND(self):
        return self.__afpText_FND

    @afpText_FND.setter
    def afpText_FND(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_FND__afpText_FND", None)
        self.__afpText_FND = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet85"):
                    opp_val = getattr(item, "afpText_triplet85", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet85", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet85"):
                    opp_val = getattr(item, "afpText_triplet85", None)
                    
                    setattr(item, "afpText_triplet85", self)
                    

class afpText_EPS(structuredField):

    def __init__(self, PsegName: str):
        self.PsegName = PsegName
        
    @property
    def PsegName(self) -> str:
        return self.__PsegName

    @PsegName.setter
    def PsegName(self, PsegName: str):
        self.__PsegName = PsegName

class afpText_EFN(structuredField):

    def __init__(self, RSName: str):
        self.RSName = RSName
        
    @property
    def RSName(self) -> str:
        return self.__RSName

    @RSName.setter
    def RSName(self, RSName: str):
        self.__RSName = RSName

class afpText_EBC(structuredField):

    def __init__(self, BCdoName: str, afpText_EBC: set["afpText_triplet"] = None):
        self.BCdoName = BCdoName
        self.afpText_EBC = afpText_EBC if afpText_EBC is not None else set()
        
    @property
    def BCdoName(self) -> str:
        return self.__BCdoName

    @BCdoName.setter
    def BCdoName(self, BCdoName: str):
        self.__BCdoName = BCdoName

    @property
    def afpText_EBC(self):
        return self.__afpText_EBC

    @afpText_EBC.setter
    def afpText_EBC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_EBC__afpText_EBC", None)
        self.__afpText_EBC = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet57"):
                    opp_val = getattr(item, "afpText_triplet57", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet57"):
                    opp_val = getattr(item, "afpText_triplet57", None)
                    
                    setattr(item, "afpText_triplet57", self)
                    

class afpText_FNI(structuredField):

    pass
class afpText_LLE(structuredField):

    def __init__(self, LnkType: str, afpText_LLE: set["afpText_LLERG"] = None):
        self.LnkType = LnkType
        self.afpText_LLE = afpText_LLE if afpText_LLE is not None else set()
        
    @property
    def LnkType(self) -> str:
        return self.__LnkType

    @LnkType.setter
    def LnkType(self, LnkType: str):
        self.__LnkType = LnkType

    @property
    def afpText_LLE(self):
        return self.__afpText_LLE

    @afpText_LLE.setter
    def afpText_LLE(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_LLE__afpText_LLE", None)
        self.__afpText_LLE = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_LLERG"):
                    opp_val = getattr(item, "afpText_LLERG", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_LLERG", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_LLERG"):
                    opp_val = getattr(item, "afpText_LLERG", None)
                    
                    setattr(item, "afpText_LLERG", self)
                    

class afpText_MMC(structuredField):

    def __init__(self, MMCid: str, PARAMETER1: str, afpText_MMC: set["afpText_MMCRG"] = None):
        self.MMCid = MMCid
        self.PARAMETER1 = PARAMETER1
        self.afpText_MMC = afpText_MMC if afpText_MMC is not None else set()
        
    @property
    def MMCid(self) -> str:
        return self.__MMCid

    @MMCid.setter
    def MMCid(self, MMCid: str):
        self.__MMCid = MMCid

    @property
    def PARAMETER1(self) -> str:
        return self.__PARAMETER1

    @PARAMETER1.setter
    def PARAMETER1(self, PARAMETER1: str):
        self.__PARAMETER1 = PARAMETER1

    @property
    def afpText_MMC(self):
        return self.__afpText_MMC

    @afpText_MMC.setter
    def afpText_MMC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_MMC__afpText_MMC", None)
        self.__afpText_MMC = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_MMCRG"):
                    opp_val = getattr(item, "afpText_MMCRG", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_MMCRG", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_MMCRG"):
                    opp_val = getattr(item, "afpText_MMCRG", None)
                    
                    setattr(item, "afpText_MMCRG", self)
                    

class afpText_PGP(structuredField):

    def __init__(self, Constant: str, afpText_PGP: set["afpText_PGPRG"] = None):
        self.Constant = Constant
        self.afpText_PGP = afpText_PGP if afpText_PGP is not None else set()
        
    @property
    def Constant(self) -> str:
        return self.__Constant

    @Constant.setter
    def Constant(self, Constant: str):
        self.__Constant = Constant

    @property
    def afpText_PGP(self):
        return self.__afpText_PGP

    @afpText_PGP.setter
    def afpText_PGP(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_PGP__afpText_PGP", None)
        self.__afpText_PGP = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_PGPRG"):
                    opp_val = getattr(item, "afpText_PGPRG", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_PGPRG", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_PGPRG"):
                    opp_val = getattr(item, "afpText_PGPRG", None)
                    
                    setattr(item, "afpText_PGPRG", self)
                    

class afpText_BCA(structuredField):

    def __init__(self, CATName: str, afpText_BCA: set["afpText_triplet"] = None):
        self.CATName = CATName
        self.afpText_BCA = afpText_BCA if afpText_BCA is not None else set()
        
    @property
    def CATName(self) -> str:
        return self.__CATName

    @CATName.setter
    def CATName(self, CATName: str):
        self.__CATName = CATName

    @property
    def afpText_BCA(self):
        return self.__afpText_BCA

    @afpText_BCA.setter
    def afpText_BCA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_BCA__afpText_BCA", None)
        self.__afpText_BCA = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet5"):
                    opp_val = getattr(item, "afpText_triplet5", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet5"):
                    opp_val = getattr(item, "afpText_triplet5", None)
                    
                    setattr(item, "afpText_triplet5", self)
                    

class afpText_GAD(structuredField):

    def __init__(self, GOCAdat: str):
        self.GOCAdat = GOCAdat
        
    @property
    def GOCAdat(self) -> str:
        return self.__GOCAdat

    @GOCAdat.setter
    def GOCAdat(self, GOCAdat: str):
        self.__GOCAdat = GOCAdat

class afpText_IPG(structuredField):

    def __init__(self, PgName: str, IPgFlgs: str, afpText_IPG: set["afpText_triplet"] = None):
        self.PgName = PgName
        self.IPgFlgs = IPgFlgs
        self.afpText_IPG = afpText_IPG if afpText_IPG is not None else set()
        
    @property
    def IPgFlgs(self) -> str:
        return self.__IPgFlgs

    @IPgFlgs.setter
    def IPgFlgs(self, IPgFlgs: str):
        self.__IPgFlgs = IPgFlgs

    @property
    def PgName(self) -> str:
        return self.__PgName

    @PgName.setter
    def PgName(self, PgName: str):
        self.__PgName = PgName

    @property
    def afpText_IPG(self):
        return self.__afpText_IPG

    @afpText_IPG.setter
    def afpText_IPG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_IPG__afpText_IPG", None)
        self.__afpText_IPG = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet101"):
                    opp_val = getattr(item, "afpText_triplet101", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet101"):
                    opp_val = getattr(item, "afpText_triplet101", None)
                    
                    setattr(item, "afpText_triplet101", self)
                    

class afpText_IOC(structuredField):

    def __init__(self, XoaOset: str, YoaOset: str, XoaOrent: str, YoaOrent: str, ConData1: str, XMap: str, YMap: str, ConData2: str):
        self.XoaOset = XoaOset
        self.YoaOset = YoaOset
        self.XoaOrent = XoaOrent
        self.YoaOrent = YoaOrent
        self.ConData1 = ConData1
        self.XMap = XMap
        self.YMap = YMap
        self.ConData2 = ConData2
        
    @property
    def ConData1(self) -> str:
        return self.__ConData1

    @ConData1.setter
    def ConData1(self, ConData1: str):
        self.__ConData1 = ConData1

    @property
    def ConData2(self) -> str:
        return self.__ConData2

    @ConData2.setter
    def ConData2(self, ConData2: str):
        self.__ConData2 = ConData2

    @property
    def YMap(self) -> str:
        return self.__YMap

    @YMap.setter
    def YMap(self, YMap: str):
        self.__YMap = YMap

    @property
    def XoaOset(self) -> str:
        return self.__XoaOset

    @XoaOset.setter
    def XoaOset(self, XoaOset: str):
        self.__XoaOset = XoaOset

    @property
    def YoaOset(self) -> str:
        return self.__YoaOset

    @YoaOset.setter
    def YoaOset(self, YoaOset: str):
        self.__YoaOset = YoaOset

    @property
    def XoaOrent(self) -> str:
        return self.__XoaOrent

    @XoaOrent.setter
    def XoaOrent(self, XoaOrent: str):
        self.__XoaOrent = XoaOrent

    @property
    def YoaOrent(self) -> str:
        return self.__YoaOrent

    @YoaOrent.setter
    def YoaOrent(self, YoaOrent: str):
        self.__YoaOrent = YoaOrent

    @property
    def XMap(self) -> str:
        return self.__XMap

    @XMap.setter
    def XMap(self, XMap: str):
        self.__XMap = XMap

class afpText_BCP(structuredField):

    def __init__(self, RSName: str, afpText_BCP: set["afpText_triplet"] = None):
        self.RSName = RSName
        self.afpText_BCP = afpText_BCP if afpText_BCP is not None else set()
        
    @property
    def RSName(self) -> str:
        return self.__RSName

    @RSName.setter
    def RSName(self, RSName: str):
        self.__RSName = RSName

    @property
    def afpText_BCP(self):
        return self.__afpText_BCP

    @afpText_BCP.setter
    def afpText_BCP(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afpText_BCP__afpText_BCP", None)
        self.__afpText_BCP = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afpText_triplet7"):
                    opp_val = getattr(item, "afpText_triplet7", None)
                    
                    if opp_val == self:
                        setattr(item, "afpText_triplet7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afpText_triplet7"):
                    opp_val = getattr(item, "afpText_triplet7", None)
                    
                    setattr(item, "afpText_triplet7", self)
                    

class afpText_IEL(structuredField):

    pass
class afpText_LineData(structuredField):

    def __init__(self, linedata: str):
        self.linedata = linedata
        
    @property
    def linedata(self) -> str:
        return self.__linedata

    @linedata.setter
    def linedata(self, linedata: str):
        self.__linedata = linedata

class afpText_structuredField:

    pass