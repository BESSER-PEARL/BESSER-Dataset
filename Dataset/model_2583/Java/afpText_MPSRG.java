





import java.util.List;
import java.util.ArrayList;

public class afpText_MPSRG  {

    private String PsegName;
    private String Reserved;





    private afpText_MPS afptext_mps;


    public afpText_MPSRG(
        String PsegName,        String Reserved    ) {
        this.PsegName = PsegName;
        this.Reserved = Reserved;
    }


    public String getPsegname() {
        return PsegName;
    }

    public void setPsegname(String PsegName) {
        this.PsegName = PsegName;
    }
    public String getReserved() {
        return Reserved;
    }

    public void setReserved(String Reserved) {
        this.Reserved = Reserved;
    }

    public afpText_MPS getAfptext_mps() {
        return afptext_mps;
    }

    public void setAfptext_mps(afpText_MPS afptext_mps) {
        this.afptext_mps = afptext_mps;
    }

}