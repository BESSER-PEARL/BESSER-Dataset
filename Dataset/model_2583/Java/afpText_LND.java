





import java.util.List;
import java.util.ArrayList;

public class afpText_LND extends structuredField {

    private String NLNDccp;
    private String SubpgID;
    private String CCPID;
    private String NLNDskp;
    private String TxtColor;
    private String BPos;
    private String TxtOrent;
    private String ChnlCde;
    private String FntLID;
    private String DataStrt;
    private String NLNDreu;
    private String NLNDsp;
    private String SupName;
    private String SOLid;
    private String IPos;
    private String LNDFlgs;
    private String DataLgth;



    public afpText_LND(
        String NLNDccp,        String SubpgID,        String CCPID,        String NLNDskp,        String TxtColor,        String BPos,        String TxtOrent,        String ChnlCde,        String FntLID,        String DataStrt,        String NLNDreu,        String NLNDsp,        String SupName,        String SOLid,        String IPos,        String LNDFlgs,        String DataLgth    ) {
        super(
        );
        this.NLNDccp = NLNDccp;
        this.SubpgID = SubpgID;
        this.CCPID = CCPID;
        this.NLNDskp = NLNDskp;
        this.TxtColor = TxtColor;
        this.BPos = BPos;
        this.TxtOrent = TxtOrent;
        this.ChnlCde = ChnlCde;
        this.FntLID = FntLID;
        this.DataStrt = DataStrt;
        this.NLNDreu = NLNDreu;
        this.NLNDsp = NLNDsp;
        this.SupName = SupName;
        this.SOLid = SOLid;
        this.IPos = IPos;
        this.LNDFlgs = LNDFlgs;
        this.DataLgth = DataLgth;
    }


    public String getNlndccp() {
        return NLNDccp;
    }

    public void setNlndccp(String NLNDccp) {
        this.NLNDccp = NLNDccp;
    }
    public String getSubpgid() {
        return SubpgID;
    }

    public void setSubpgid(String SubpgID) {
        this.SubpgID = SubpgID;
    }
    public String getCcpid() {
        return CCPID;
    }

    public void setCcpid(String CCPID) {
        this.CCPID = CCPID;
    }
    public String getNlndskp() {
        return NLNDskp;
    }

    public void setNlndskp(String NLNDskp) {
        this.NLNDskp = NLNDskp;
    }
    public String getTxtcolor() {
        return TxtColor;
    }

    public void setTxtcolor(String TxtColor) {
        this.TxtColor = TxtColor;
    }
    public String getBpos() {
        return BPos;
    }

    public void setBpos(String BPos) {
        this.BPos = BPos;
    }
    public String getTxtorent() {
        return TxtOrent;
    }

    public void setTxtorent(String TxtOrent) {
        this.TxtOrent = TxtOrent;
    }
    public String getChnlcde() {
        return ChnlCde;
    }

    public void setChnlcde(String ChnlCde) {
        this.ChnlCde = ChnlCde;
    }
    public String getFntlid() {
        return FntLID;
    }

    public void setFntlid(String FntLID) {
        this.FntLID = FntLID;
    }
    public String getDatastrt() {
        return DataStrt;
    }

    public void setDatastrt(String DataStrt) {
        this.DataStrt = DataStrt;
    }
    public String getNlndreu() {
        return NLNDreu;
    }

    public void setNlndreu(String NLNDreu) {
        this.NLNDreu = NLNDreu;
    }
    public String getNlndsp() {
        return NLNDsp;
    }

    public void setNlndsp(String NLNDsp) {
        this.NLNDsp = NLNDsp;
    }
    public String getSupname() {
        return SupName;
    }

    public void setSupname(String SupName) {
        this.SupName = SupName;
    }
    public String getSolid() {
        return SOLid;
    }

    public void setSolid(String SOLid) {
        this.SOLid = SOLid;
    }
    public String getIpos() {
        return IPos;
    }

    public void setIpos(String IPos) {
        this.IPos = IPos;
    }
    public String getLndflgs() {
        return LNDFlgs;
    }

    public void setLndflgs(String LNDFlgs) {
        this.LNDFlgs = LNDFlgs;
    }
    public String getDatalgth() {
        return DataLgth;
    }

    public void setDatalgth(String DataLgth) {
        this.DataLgth = DataLgth;
    }


}