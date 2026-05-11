





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_MessageEventDefinition extends EventDefinition {






    private bpmnprof_BPMNOperation bpmnprof_bpmnoperation;




    private bpmnprof_BPMNMessage bpmnprof_bpmnmessage;


    public bpmnprof_MessageEventDefinition(
    ) {
        super(
        );
    }



    public bpmnprof_BPMNOperation getBpmnprof_bpmnoperation() {
        return bpmnprof_bpmnoperation;
    }

    public void setBpmnprof_bpmnoperation(bpmnprof_BPMNOperation bpmnprof_bpmnoperation) {
        this.bpmnprof_bpmnoperation = bpmnprof_bpmnoperation;
    }
    public bpmnprof_BPMNMessage getBpmnprof_bpmnmessage() {
        return bpmnprof_bpmnmessage;
    }

    public void setBpmnprof_bpmnmessage(bpmnprof_BPMNMessage bpmnprof_bpmnmessage) {
        this.bpmnprof_bpmnmessage = bpmnprof_bpmnmessage;
    }

}