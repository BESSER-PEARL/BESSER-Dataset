





import java.util.List;
import java.util.ArrayList;

public class afpText_GSFLW extends triplet {

    private String MH;
    private String MFR;



    public afpText_GSFLW(
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