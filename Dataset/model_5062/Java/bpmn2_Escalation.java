





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Escalation  {

    private String escalationCode;
    private String name;





    private bpmn2_ItemDefinition bpmn2_itemdefinition;




    private bpmn2_EscalationEventDefinition bpmn2_escalationeventdefinition;


    public bpmn2_Escalation(
        String escalationCode,        String name    ) {
        this.escalationCode = escalationCode;
        this.name = name;
    }


    public String getEscalationcode() {
        return escalationCode;
    }

    public void setEscalationcode(String escalationCode) {
        this.escalationCode = escalationCode;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public bpmn2_ItemDefinition getBpmn2_itemdefinition() {
        return bpmn2_itemdefinition;
    }

    public void setBpmn2_itemdefinition(bpmn2_ItemDefinition bpmn2_itemdefinition) {
        this.bpmn2_itemdefinition = bpmn2_itemdefinition;
    }
    public bpmn2_EscalationEventDefinition getBpmn2_escalationeventdefinition() {
        return bpmn2_escalationeventdefinition;
    }

    public void setBpmn2_escalationeventdefinition(bpmn2_EscalationEventDefinition bpmn2_escalationeventdefinition) {
        this.bpmn2_escalationeventdefinition = bpmn2_escalationeventdefinition;
    }

}