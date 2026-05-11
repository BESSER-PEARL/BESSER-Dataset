





import java.util.List;
import java.util.ArrayList;

public class afpText_FNIRG  {

    private String FNMCnt;
    private String BaseOset;
    private String CharInc;
    private String Reserved;
    private String DescendDp;
    private String BSpace;
    private String AscendHt;
    private String ASpace;
    private String GCGID;
    private String CSpace;
    private String Reserved2;





    private afpText_FNI afptext_fni;


    public afpText_FNIRG(
        String FNMCnt,        String BaseOset,        String CharInc,        String Reserved,        String DescendDp,        String BSpace,        String AscendHt,        String ASpace,        String GCGID,        String CSpace,        String Reserved2    ) {
        this.FNMCnt = FNMCnt;
        this.BaseOset = BaseOset;
        this.CharInc = CharInc;
        this.Reserved = Reserved;
        this.DescendDp = DescendDp;
        this.BSpace = BSpace;
        this.AscendHt = AscendHt;
        this.ASpace = ASpace;
        this.GCGID = GCGID;
        this.CSpace = CSpace;
        this.Reserved2 = Reserved2;
    }


    public String getFnmcnt() {
        return FNMCnt;
    }

    public void setFnmcnt(String FNMCnt) {
        this.FNMCnt = FNMCnt;
    }
    public String getBaseoset() {
        return BaseOset;
    }

    public void setBaseoset(String BaseOset) {
        this.BaseOset = BaseOset;
    }
    public String getCharinc() {
        return CharInc;
    }

    public void setCharinc(String CharInc) {
        this.CharInc = CharInc;
    }
    public String getReserved() {
        return Reserved;
    }

    public void setReserved(String Reserved) {
        this.Reserved = Reserved;
    }
    public String getDescenddp() {
        return DescendDp;
    }

    public void setDescenddp(String DescendDp) {
        this.DescendDp = DescendDp;
    }
    public String getBspace() {
        return BSpace;
    }

    public void setBspace(String BSpace) {
        this.BSpace = BSpace;
    }
    public String getAscendht() {
        return AscendHt;
    }

    public void setAscendht(String AscendHt) {
        this.AscendHt = AscendHt;
    }
    public String getAspace() {
        return ASpace;
    }

    public void setAspace(String ASpace) {
        this.ASpace = ASpace;
    }
    public String getGcgid() {
        return GCGID;
    }

    public void setGcgid(String GCGID) {
        this.GCGID = GCGID;
    }
    public String getCspace() {
        return CSpace;
    }

    public void setCspace(String CSpace) {
        this.CSpace = CSpace;
    }
    public String getReserved2() {
        return Reserved2;
    }

    public void setReserved2(String Reserved2) {
        this.Reserved2 = Reserved2;
    }

    public afpText_FNI getAfptext_fni() {
        return afptext_fni;
    }

    public void setAfptext_fni(afpText_FNI afptext_fni) {
        this.afptext_fni = afptext_fni;
    }

}