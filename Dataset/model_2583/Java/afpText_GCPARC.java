





import java.util.List;
import java.util.ArrayList;

public class afpText_GCPARC extends triplet {

    private String START;
    private String MFR;
    private String MH;
    private String SWEEP;
    private String YCENT;
    private String XCENT;



    public afpText_GCPARC(
        String START,        String MFR,        String MH,        String SWEEP,        String YCENT,        String XCENT    ) {
        super(
        );
        this.START = START;
        this.MFR = MFR;
        this.MH = MH;
        this.SWEEP = SWEEP;
        this.YCENT = YCENT;
        this.XCENT = XCENT;
    }


    public String getStart() {
        return START;
    }

    public void setStart(String START) {
        this.START = START;
    }
    public String getMfr() {
        return MFR;
    }

    public void setMfr(String MFR) {
        this.MFR = MFR;
    }
    public String getMh() {
        return MH;
    }

    public void setMh(String MH) {
        this.MH = MH;
    }
    public String getSweep() {
        return SWEEP;
    }

    public void setSweep(String SWEEP) {
        this.SWEEP = SWEEP;
    }
    public String getYcent() {
        return YCENT;
    }

    public void setYcent(String YCENT) {
        this.YCENT = YCENT;
    }
    public String getXcent() {
        return XCENT;
    }

    public void setXcent(String XCENT) {
        this.XCENT = XCENT;
    }


}