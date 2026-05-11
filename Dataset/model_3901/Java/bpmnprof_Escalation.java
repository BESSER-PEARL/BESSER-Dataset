





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_Escalation extends ItemDefinition {

    private String escalationCode;



    public bpmnprof_Escalation(
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


}