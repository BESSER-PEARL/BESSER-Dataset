





import java.util.List;
import java.util.ArrayList;

public class afpText_GCFARC extends triplet {

    private String MH;
    private String MFR;



    public afpText_GCFARC(
        String MH,        String MFR    ) {
        super(
        );
        this.MH = MH;
        this.MFR = MFR;
    }


    public String getMh() {
        return MH;
    }

    public void setMh(String MH) {
        this.MH = MH;
    }
    public String getMfr() {
        return MFR;
    }

    public void setMfr(String MFR) {
        this.MFR = MFR;
    }


}