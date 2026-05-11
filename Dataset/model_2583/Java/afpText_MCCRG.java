





import java.util.List;
import java.util.ArrayList;

public class afpText_MCCRG  {

    private String Stopnum;
    private String MMCid;
    private String Startnum;





    private afpText_MCC afptext_mcc;


    public afpText_MCCRG(
        String Stopnum,        String MMCid,        String Startnum    ) {
        this.Stopnum = Stopnum;
        this.MMCid = MMCid;
        this.Startnum = Startnum;
    }


    public String getStopnum() {
        return Stopnum;
    }

    public void setStopnum(String Stopnum) {
        this.Stopnum = Stopnum;
    }
    public String getMmcid() {
        return MMCid;
    }

    public void setMmcid(String MMCid) {
        this.MMCid = MMCid;
    }
    public String getStartnum() {
        return Startnum;
    }

    public void setStartnum(String Startnum) {
        this.Startnum = Startnum;
    }

    public afpText_MCC getAfptext_mcc() {
        return afptext_mcc;
    }

    public void setAfptext_mcc(afpText_MCC afptext_mcc) {
        this.afptext_mcc = afptext_mcc;
    }

}