





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_ReceiveTask extends Task {

    private String implementation;
    private String instantiate;





    private BPMNProfile_AcceptEventAction bpmnprofile_accepteventaction;




    private BPMNProfile_BPMNMessage bpmnprofile_bpmnmessage;




    private BPMNProfile_BPMNOperation bpmnprofile_bpmnoperation;


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