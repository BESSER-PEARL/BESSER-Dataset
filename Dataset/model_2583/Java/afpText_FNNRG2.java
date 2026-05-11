





import java.util.List;
import java.util.ArrayList;

public class afpText_FNNRG2 extends triplet {

    private String TSIDLen;
    private String TSID;



    public afpText_FNNRG2(
        String TSIDLen,        String TSID    ) {
        super(
        );
        this.TSIDLen = TSIDLen;
        this.TSID = TSID;
    }


    public String getTsidlen() {
        return TSIDLen;
    }

    public void setTsidlen(String TSIDLen) {
        this.TSIDLen = TSIDLen;
    }
    public String getTsid() {
        return TSID;
    }

    public void setTsid(String TSID) {
        this.TSID = TSID;
    }


}