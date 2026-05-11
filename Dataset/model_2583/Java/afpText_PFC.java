





import java.util.List;
import java.util.ArrayList;

public class afpText_PFC extends structuredField {

    private String PFCFlgs;



    public afpText_PFC(
        String PFCFlgs    ) {
        super(
        );
        this.PFCFlgs = PFCFlgs;
    }


    public String getPfcflgs() {
        return PFCFlgs;
    }

    public void setPfcflgs(String PFCFlgs) {
        this.PFCFlgs = PFCFlgs;
    }


}