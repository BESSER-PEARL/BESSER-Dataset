





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_Escalation extends ItemDefinition {

    private String escalationCode;





    private BPMNProfile_EscalationEventDefinition bpmnprofile_escalationeventdefinition;


    public BPMNProfile_Escalation(
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

    public BPMNProfile_EscalationEventDefinition getBpmnprofile_escalationeventdefinition() {
        return bpmnprofile_escalationeventdefinition;
    }

    public void setBpmnprofile_escalationeventdefinition(BPMNProfile_EscalationEventDefinition bpmnprofile_escalationeventdefinition) {
        this.bpmnprofile_escalationeventdefinition = bpmnprofile_escalationeventdefinition;
    }

}