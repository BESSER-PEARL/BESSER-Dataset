





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Escalation extends RootElement {

    private String escalationCode;





    private bpmn2_DocumentRoot bpmn2_documentroot;


    public bpmn2_Escalation(
        String escalationCode    ) {
        super(
        );
        this.escalationCode = escalationCode;
    }


    public String getEscalationcode() {
        return escalationCode;
    }

    public void setEscalationcode(String escalationCode) {
        this.escalationCode = escalationCode;
    }

    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}