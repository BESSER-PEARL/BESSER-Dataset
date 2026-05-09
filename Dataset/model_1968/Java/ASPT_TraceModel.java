





import java.util.List;
import java.util.ArrayList;

public class ASPT_TraceModel  {

    private String MMS;
    private String ID;



    public ASPT_TraceModel(
        String MMS,        String ID    ) {
        this.MMS = MMS;
        this.ID = ID;
    }


    public String getMms() {
        return MMS;
    }

    public void setMms(String MMS) {
        this.MMS = MMS;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }


}