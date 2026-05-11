





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_ReceiveTask extends Task {

    private String implementation;
    private String instantiate;





    private BPMNProfile_AcceptEventAction bpmnprofile_accepteventaction;


    public BPMNProfile_ReceiveTask(
        String implementation,        String instantiate    ) {
        super(
        );
        this.implementation = implementation;
        this.instantiate = instantiate;
    }


    public String getImplementation() {
        return implementation;
    }

    public void setImplementation(String implementation) {
        this.implementation = implementation;
    }
    public String getInstantiate() {
        return instantiate;
    }

    public void setInstantiate(String instantiate) {
        this.instantiate = instantiate;
    }

    public BPMNProfile_AcceptEventAction getBpmnprofile_accepteventaction() {
        return bpmnprofile_accepteventaction;
    }

    public void setBpmnprofile_accepteventaction(BPMNProfile_AcceptEventAction bpmnprofile_accepteventaction) {
        this.bpmnprofile_accepteventaction = bpmnprofile_accepteventaction;
    }

}