





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_ServiceTask extends Task {

    private String implementation;





    private BPMNProfile_BPMNOperation bpmnprofile_bpmnoperation;




    private BPMNProfile_CallOperationAction bpmnprofile_calloperationaction;


    public BPMNProfile_ServiceTask(
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

    public BPMNProfile_BPMNOperation getBpmnprofile_bpmnoperation() {
        return bpmnprofile_bpmnoperation;
    }

    public void setBpmnprofile_bpmnoperation(BPMNProfile_BPMNOperation bpmnprofile_bpmnoperation) {
        this.bpmnprofile_bpmnoperation = bpmnprofile_bpmnoperation;
    }
    public BPMNProfile_CallOperationAction getBpmnprofile_calloperationaction() {
        return bpmnprofile_calloperationaction;
    }

    public void setBpmnprofile_calloperationaction(BPMNProfile_CallOperationAction bpmnprofile_calloperationaction) {
        this.bpmnprofile_calloperationaction = bpmnprofile_calloperationaction;
    }

}