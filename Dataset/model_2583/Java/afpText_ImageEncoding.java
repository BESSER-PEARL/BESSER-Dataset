





import java.util.List;
import java.util.ArrayList;

public class afpText_ImageEncoding extends triplet {

    private String BITORDR;
    private String RECID;
    private String COMPRID;



    public afpText_ImageEncoding(
        String BITORDR,        String RECID,        String COMPRID    ) {
        super(
        );
        this.BITORDR = BITORDR;
        this.RECID = RECID;
        this.COMPRID = COMPRID;
    }


    public String getBitordr() {
        return BITORDR;
    }

    public void setBitordr(String BITORDR) {
        this.BITORDR = BITORDR;
    }
    public String getRecid() {
        return RECID;
    }

    public void setRecid(String RECID) {
        this.RECID = RECID;
    }
    public String getComprid() {
        return COMPRID;
    }

    public void setComprid(String COMPRID) {
        this.COMPRID = COMPRID;
    }


}