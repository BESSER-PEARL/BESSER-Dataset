





import java.util.List;
import java.util.ArrayList;

public class afpText_FND extends structuredField {

    private String DsnSubCls;
    private String FtWtClass;
    private String MinPtSize;
    private String GCSID;
    private String MinHSize;
    private String NomPtSize;
    private String Reserved1;
    private String NomHSize;
    private String TypeFcDesc;
    private String FtWdClass;
    private String DsnSpcGrp;
    private String FtDsFlags;
    private String DsnGenCls;
    private String FGID;
    private String MaxPtSize;
    private String MaxHSize;
    private String Reserved2;



    public afpText_FND(
        String DsnSubCls,        String FtWtClass,        String MinPtSize,        String GCSID,        String MinHSize,        String NomPtSize,        String Reserved1,        String NomHSize,        String TypeFcDesc,        String FtWdClass,        String DsnSpcGrp,        String FtDsFlags,        String DsnGenCls,        String FGID,        String MaxPtSize,        String MaxHSize,        String Reserved2    ) {
        super(
        );
        this.DsnSubCls = DsnSubCls;
        this.FtWtClass = FtWtClass;
        this.MinPtSize = MinPtSize;
        this.GCSID = GCSID;
        this.MinHSize = MinHSize;
        this.NomPtSize = NomPtSize;
        this.Reserved1 = Reserved1;
        this.NomHSize = NomHSize;
        this.TypeFcDesc = TypeFcDesc;
        this.FtWdClass = FtWdClass;
        this.DsnSpcGrp = DsnSpcGrp;
        this.FtDsFlags = FtDsFlags;
        this.DsnGenCls = DsnGenCls;
        this.FGID = FGID;
        this.MaxPtSize = MaxPtSize;
        this.MaxHSize = MaxHSize;
        this.Reserved2 = Reserved2;
    }


    public String getDsnsubcls() {
        return DsnSubCls;
    }

    public void setDsnsubcls(String DsnSubCls) {
        this.DsnSubCls = DsnSubCls;
    }
    public String getFtwtclass() {
        return FtWtClass;
    }

    public void setFtwtclass(String FtWtClass) {
        this.FtWtClass = FtWtClass;
    }
    public String getMinptsize() {
        return MinPtSize;
    }

    public void setMinptsize(String MinPtSize) {
        this.MinPtSize = MinPtSize;
    }
    public String getGcsid() {
        return GCSID;
    }

    public void setGcsid(String GCSID) {
        this.GCSID = GCSID;
    }
    public String getMinhsize() {
        return MinHSize;
    }

    public void setMinhsize(String MinHSize) {
        this.MinHSize = MinHSize;
    }
    public String getNomptsize() {
        return NomPtSize;
    }

    public void setNomptsize(String NomPtSize) {
        this.NomPtSize = NomPtSize;
    }
    public String getReserved1() {
        return Reserved1;
    }

    public void setReserved1(String Reserved1) {
        this.Reserved1 = Reserved1;
    }
    public String getNomhsize() {
        return NomHSize;
    }

    public void setNomhsize(String NomHSize) {
        this.NomHSize = NomHSize;
    }
    public String getTypefcdesc() {
        return TypeFcDesc;
    }

    public void setTypefcdesc(String TypeFcDesc) {
        this.TypeFcDesc = TypeFcDesc;
    }
    public String getFtwdclass() {
        return FtWdClass;
    }

    public void setFtwdclass(String FtWdClass) {
        this.FtWdClass = FtWdClass;
    }
    public String getDsnspcgrp() {
        return DsnSpcGrp;
    }

    public void setDsnspcgrp(String DsnSpcGrp) {
        this.DsnSpcGrp = DsnSpcGrp;
    }
    public String getFtdsflags() {
        return FtDsFlags;
    }

    public void setFtdsflags(String FtDsFlags) {
        this.FtDsFlags = FtDsFlags;
    }
    public String getDsngencls() {
        return DsnGenCls;
    }

    public void setDsngencls(String DsnGenCls) {
        this.DsnGenCls = DsnGenCls;
    }
    public String getFgid() {
        return FGID;
    }

    public void setFgid(String FGID) {
        this.FGID = FGID;
    }
    public String getMaxptsize() {
        return MaxPtSize;
    }

    public void setMaxptsize(String MaxPtSize) {
        this.MaxPtSize = MaxPtSize;
    }
    public String getMaxhsize() {
        return MaxHSize;
    }

    public void setMaxhsize(String MaxHSize) {
        this.MaxHSize = MaxHSize;
    }
    public String getReserved2() {
        return Reserved2;
    }

    public void setReserved2(String Reserved2) {
        this.Reserved2 = Reserved2;
    }


}