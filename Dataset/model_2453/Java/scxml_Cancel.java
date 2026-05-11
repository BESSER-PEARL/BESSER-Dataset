





import java.util.List;
import java.util.ArrayList;

public class scxml_Cancel  {

    private String sendidexpr;
    private String sendid;





    private scxml_OnExit scxml_onexit;




    private scxml_If scxml_if;




    private scxml_Finalize scxml_finalize;




    private scxml_OnEntry scxml_onentry;


    public scxml_Cancel(
        String sendidexpr,        String sendid    ) {
        this.sendidexpr = sendidexpr;
        this.sendid = sendid;
    }


    public String getSendidexpr() {
        return sendidexpr;
    }

    public void setSendidexpr(String sendidexpr) {
        this.sendidexpr = sendidexpr;
    }
    public String getSendid() {
        return sendid;
    }

    public void setSendid(String sendid) {
        this.sendid = sendid;
    }

    public scxml_OnExit getScxml_onexit() {
        return scxml_onexit;
    }

    public void setScxml_onexit(scxml_OnExit scxml_onexit) {
        this.scxml_onexit = scxml_onexit;
    }
    public scxml_If getScxml_if() {
        return scxml_if;
    }

    public void setScxml_if(scxml_If scxml_if) {
        this.scxml_if = scxml_if;
    }
    public scxml_Finalize getScxml_finalize() {
        return scxml_finalize;
    }

    public void setScxml_finalize(scxml_Finalize scxml_finalize) {
        this.scxml_finalize = scxml_finalize;
    }
    public scxml_OnEntry getScxml_onentry() {
        return scxml_onentry;
    }

    public void setScxml_onentry(scxml_OnEntry scxml_onentry) {
        this.scxml_onentry = scxml_onentry;
    }

}