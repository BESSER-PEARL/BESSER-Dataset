





import java.util.List;
import java.util.ArrayList;

public class afpText_RPS extends triplet {

    private String RLENGTH;
    private String RPTDATA;



    public afpText_RPS(
        String RLENGTH,        String RPTDATA    ) {
        super(
        );
        this.RLENGTH = RLENGTH;
        this.RPTDATA = RPTDATA;
    }


    public String getRlength() {
        return RLENGTH;
    }

    public void setRlength(String RLENGTH) {
        this.RLENGTH = RLENGTH;
    }
    public String getRptdata() {
        return RPTDATA;
    }

    public void setRptdata(String RPTDATA) {
        this.RPTDATA = RPTDATA;
    }


}