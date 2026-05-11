





import java.util.List;
import java.util.ArrayList;

public class scxml_Cancel  {

    private String sendidexpr;
    private String sendid;





    private scxml_ExecutableContent scxml_executablecontent;


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

    public scxml_ExecutableContent getScxml_executablecontent() {
        return scxml_executablecontent;
    }

    public void setScxml_executablecontent(scxml_ExecutableContent scxml_executablecontent) {
        this.scxml_executablecontent = scxml_executablecontent;
    }

}