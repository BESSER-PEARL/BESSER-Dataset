





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_Escalation extends BPMNBase {

    private String escalationCode;
    private String name;





    private BPMN2Model_ItemDefinition bpmn2model_itemdefinition;




    private BPMN2Model_DocumentRoot bpmn2model_documentroot;




    private BPMN2Model_EscalationEventDefinition bpmn2model_escalationeventdefinition;


    public BPMN2Model_Escalation(
        String escalationCode,        String name    ) {
        super(
        );
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

    public BPMN2Model_ItemDefinition getBpmn2model_itemdefinition() {
        return bpmn2model_itemdefinition;
    }

    public void setBpmn2model_itemdefinition(BPMN2Model_ItemDefinition bpmn2model_itemdefinition) {
        this.bpmn2model_itemdefinition = bpmn2model_itemdefinition;
    }
    public BPMN2Model_DocumentRoot getBpmn2model_documentroot() {
        return bpmn2model_documentroot;
    }

    public void setBpmn2model_documentroot(BPMN2Model_DocumentRoot bpmn2model_documentroot) {
        this.bpmn2model_documentroot = bpmn2model_documentroot;
    }
    public BPMN2Model_EscalationEventDefinition getBpmn2model_escalationeventdefinition() {
        return bpmn2model_escalationeventdefinition;
    }

    public void setBpmn2model_escalationeventdefinition(BPMN2Model_EscalationEventDefinition bpmn2model_escalationeventdefinition) {
        this.bpmn2model_escalationeventdefinition = bpmn2model_escalationeventdefinition;
    }

}