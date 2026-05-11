





import java.util.List;
import java.util.ArrayList;

public class afpText_MFC extends structuredField {

    private String MFCFlgs;
    private String MFCScpe;
    private String MedColl;



    public afpText_MFC(
        String MFCFlgs,        String MFCScpe,        String MedColl    ) {
        super(
        );
        this.MFCFlgs = MFCFlgs;
        this.MFCScpe = MFCScpe;
        this.MedColl = MedColl;
    }


    public String getMfcflgs() {
        return MFCFlgs;
    }

    public void setMfcflgs(String MFCFlgs) {
        this.MFCFlgs = MFCFlgs;
    }
    public String getMfcscpe() {
        return MFCScpe;
    }

    public void setMfcscpe(String MFCScpe) {
        this.MFCScpe = MFCScpe;
    }
    public String getMedcoll() {
        return MedColl;
    }

    public void setMedcoll(String MedColl) {
        this.MedColl = MedColl;
    }


}