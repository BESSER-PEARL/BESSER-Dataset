





import java.util.List;
import java.util.ArrayList;

public class afpText_GFARC extends triplet {

    private String MFR;
    private String XPOS;
    private String MH;
    private String YPOS;



    public afpText_GFARC(
        String MFR,        String XPOS,        String MH,        String YPOS    ) {
        super(
        );
        this.MFR = MFR;
        this.XPOS = XPOS;
        this.MH = MH;
        this.YPOS = YPOS;
    }


    public String getMfr() {
        return MFR;
    }

    public void setMfr(String MFR) {
        this.MFR = MFR;
    }
    public String getXpos() {
        return XPOS;
    }

    public void setXpos(String XPOS) {
        this.XPOS = XPOS;
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


}