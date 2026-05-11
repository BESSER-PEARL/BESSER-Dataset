





import java.util.List;
import java.util.ArrayList;

public class bpmn2_EscalationEventDefinition extends EventDefinition {






    private bpmn2_Escalation bpmn2_escalation;




    private bpmn2_DocumentRoot bpmn2_documentroot;


    public bpmn2_EscalationEventDefinition(
    ) {
        super(
        );
    }



    public bpmn2_Escalation getBpmn2_escalation() {
        return bpmn2_escalation;
    }

    public void setBpmn2_escalation(bpmn2_Escalation bpmn2_escalation) {
        this.bpmn2_escalation = bpmn2_escalation;
    }
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}