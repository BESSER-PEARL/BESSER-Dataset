





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_BPMNOperation extends BaseElement {






    private BPMNProfile_ReceiveTask bpmnprofile_receivetask;




    private BPMNProfile_SendTask bpmnprofile_sendtask;




    private BPMNProfile_ServiceTask bpmnprofile_servicetask;




    private BPMNProfile_MessageEventDefinition bpmnprofile_messageeventdefinition;


    public BPMNProfile_BPMNOperation(
    ) {
        super(
        );
    }



    public BPMNProfile_ReceiveTask getBpmnprofile_receivetask() {
        return bpmnprofile_receivetask;
    }

    public void setBpmnprofile_receivetask(BPMNProfile_ReceiveTask bpmnprofile_receivetask) {
        this.bpmnprofile_receivetask = bpmnprofile_receivetask;
    }
    public BPMNProfile_SendTask getBpmnprofile_sendtask() {
        return bpmnprofile_sendtask;
    }

    public void setBpmnprofile_sendtask(BPMNProfile_SendTask bpmnprofile_sendtask) {
        this.bpmnprofile_sendtask = bpmnprofile_sendtask;
    }
    public BPMNProfile_ServiceTask getBpmnprofile_servicetask() {
        return bpmnprofile_servicetask;
    }

    public void setBpmnprofile_servicetask(BPMNProfile_ServiceTask bpmnprofile_servicetask) {
        this.bpmnprofile_servicetask = bpmnprofile_servicetask;
    }
    public BPMNProfile_MessageEventDefinition getBpmnprofile_messageeventdefinition() {
        return bpmnprofile_messageeventdefinition;
    }

    public void setBpmnprofile_messageeventdefinition(BPMNProfile_MessageEventDefinition bpmnprofile_messageeventdefinition) {
        this.bpmnprofile_messageeventdefinition = bpmnprofile_messageeventdefinition;
    }

}