





import java.util.List;
import java.util.ArrayList;

public class afpText_ExternalAlgorithmRG  {

    private String DIRCTN;
    private String PADALMT;
    private String PADBDRY;



    public afpText_ExternalAlgorithmRG(
        String DIRCTN,        String PADALMT,        String PADBDRY    ) {
        this.DIRCTN = DIRCTN;
        this.PADALMT = PADALMT;
        this.PADBDRY = PADBDRY;
    }


    public String getDirctn() {
        return DIRCTN;
    }

    public void setDirctn(String DIRCTN) {
        this.DIRCTN = DIRCTN;
    }
    public String getPadalmt() {
        return PADALMT;
    }

    public void setPadalmt(String PADALMT) {
        this.PADALMT = PADALMT;
    }
    public String getPadbdry() {
        return PADBDRY;
    }

    public void setPadbdry(String PADBDRY) {
        this.PADBDRY = PADBDRY;
    }


}