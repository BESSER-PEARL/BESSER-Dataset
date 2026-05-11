





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Message extends RootElement {

    private String name;





    private bpmn2_ReceiveTask bpmn2_receivetask;




    private bpmn2_MessageEventDefinition bpmn2_messageeventdefinition;




    private bpmn2_SendTask bpmn2_sendtask;


    public bpmn2_Message(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public bpmn2_ReceiveTask getBpmn2_receivetask() {
        return bpmn2_receivetask;
    }

    public void setBpmn2_receivetask(bpmn2_ReceiveTask bpmn2_receivetask) {
        this.bpmn2_receivetask = bpmn2_receivetask;
    }
    public bpmn2_MessageEventDefinition getBpmn2_messageeventdefinition() {
        return bpmn2_messageeventdefinition;
    }

    public void setBpmn2_messageeventdefinition(bpmn2_MessageEventDefinition bpmn2_messageeventdefinition) {
        this.bpmn2_messageeventdefinition = bpmn2_messageeventdefinition;
    }
    public bpmn2_SendTask getBpmn2_sendtask() {
        return bpmn2_sendtask;
    }

    public void setBpmn2_sendtask(bpmn2_SendTask bpmn2_sendtask) {
        this.bpmn2_sendtask = bpmn2_sendtask;
    }

}