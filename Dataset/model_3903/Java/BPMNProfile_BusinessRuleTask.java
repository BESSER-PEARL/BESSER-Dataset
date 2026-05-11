





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_BusinessRuleTask extends Task {

    private String implementation;





    private BPMNProfile_OpaqueAction bpmnprofile_opaqueaction;


    public BPMNProfile_BusinessRuleTask(
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

    public BPMNProfile_OpaqueAction getBpmnprofile_opaqueaction() {
        return bpmnprofile_opaqueaction;
    }

    public void setBpmnprofile_opaqueaction(BPMNProfile_OpaqueAction bpmnprofile_opaqueaction) {
        this.bpmnprofile_opaqueaction = bpmnprofile_opaqueaction;
    }

}