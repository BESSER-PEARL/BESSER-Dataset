





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_SendTask extends Task {

    private String implementation;





    private BPMNProfile_CallOperationAction bpmnprofile_calloperationaction;




    private BPMNProfile_BPMNMessage bpmnprofile_bpmnmessage;




    private BPMNProfile_BPMNOperation bpmnprofile_bpmnoperation;


    public BPMNProfile_SendTask(
        String implementation    ) {
        super(
        );
        this.implementation = implementation;
    }


    public String getImplementation() {
        return implementation;
    }

    public void setImplementation(String implementation) {
        this.implementation = implementation;
    }

    public BPMNProfile_CallOperationAction getBpmnprofile_calloperationaction() {
        return bpmnprofile_calloperationaction;
    }

    public void setBpmnprofile_calloperationaction(BPMNProfile_CallOperationAction bpmnprofile_calloperationaction) {
        this.bpmnprofile_calloperationaction = bpmnprofile_calloperationaction;
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