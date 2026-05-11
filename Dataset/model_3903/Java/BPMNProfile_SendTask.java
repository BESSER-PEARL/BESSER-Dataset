





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_SendTask extends Task {

    private String implementation;





    private BPMNProfile_CallOperationAction bpmnprofile_calloperationaction;


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

}