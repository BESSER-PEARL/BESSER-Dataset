





import java.util.List;
import java.util.ArrayList;

public class afpText_GPARC extends triplet {

    private String MH;
    private String YPOS;
    private String SWEEP;
    private String XCENT;
    private String XPOS;
    private String START;
    private String MFR;
    private String YCENT;



    public afpText_GPARC(
        String MH,        String YPOS,        String SWEEP,        String XCENT,        String XPOS,        String START,        String MFR,        String YCENT    ) {
        super(
        );
        this.MH = MH;
        this.YPOS = YPOS;
        this.SWEEP = SWEEP;
        this.XCENT = XCENT;
        this.XPOS = XPOS;
        this.START = START;
        this.MFR = MFR;
        this.YCENT = YCENT;
    }


    public String getMh() {
        return MH;
    }

    public void setMh(String MH) {
        this.MH = MH;
    }
    public String getYpos() {
        return YPOS;
    }

    public void setYpos(String YPOS) {
        this.YPOS = YPOS;
    }
    public String getSweep() {
        return SWEEP;
    }

    public void setSweep(String SWEEP) {
        this.SWEEP = SWEEP;
    }
    public String getXcent() {
        return XCENT;
    }

    public void setXcent(String XCENT) {
        this.XCENT = XCENT;
    }
    public String getXpos() {
        return XPOS;
    }

    public void setXpos(String XPOS) {
        this.XPOS = XPOS;
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
    public String getYcent() {
        return YCENT;
    }

    public void setYcent(String YCENT) {
        this.YCENT = YCENT;
    }


}