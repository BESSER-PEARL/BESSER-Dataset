





import java.util.List;
import java.util.ArrayList;

public class afpText_MMC extends structuredField {

    private String MMCid;
    private String PARAMETER1;



    public afpText_MMC(
        String MMCid,        String PARAMETER1    ) {
        super(
        );
        this.MMCid = MMCid;
        this.PARAMETER1 = PARAMETER1;
    }


    public String getMmcid() {
        return MMCid;
    }

    public void setMmcid(String MMCid) {
        this.MMCid = MMCid;
    }
    public String getParameter1() {
        return PARAMETER1;
    }

    public void setParameter1(String PARAMETER1) {
        this.PARAMETER1 = PARAMETER1;
    }


}