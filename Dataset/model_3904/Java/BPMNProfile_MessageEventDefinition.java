





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_MessageEventDefinition extends EventDefinition {






    private BPMNProfile_BPMNMessage bpmnprofile_bpmnmessage;




    private BPMNProfile_BPMNOperation bpmnprofile_bpmnoperation;


    public BPMNProfile_MessageEventDefinition(
    ) {
        super(
        );
    }



    public BPMNProfile_BPMNMessage getBpmnprofile_bpmnmessage() {
        return bpmnprofile_bpmnmessage;
    }

    public void setBpmnprofile_bpmnmessage(BPMNProfile_BPMNMessage bpmnprofile_bpmnmessage) {
        this.bpmnprofile_bpmnmessage = bpmnprofile_bpmnmessage;
    }
    public BPMNProfile_BPMNOperation getBpmnprofile_bpmnoperation() {
        return bpmnprofile_bpmnoperation;
    }

    public void setBpmnprofile_bpmnoperation(BPMNProfile_BPMNOperation bpmnprofile_bpmnoperation) {
        this.bpmnprofile_bpmnoperation = bpmnprofile_bpmnoperation;
    }

}