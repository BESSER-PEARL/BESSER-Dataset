





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_UserTask extends Task {

    private String implementation;





    private List<BPMNProfile_Rendering> bpmnprofile_renderings;




    private BPMNProfile_OpaqueAction bpmnprofile_opaqueaction;


    public BPMNProfile_UserTask(
        String implementation    ) {
        super(
        );
        this.implementation = implementation;
        this.bpmnprofile_renderings = new ArrayList<>();
    }

    public BPMNProfile_UserTask(
        String implementation        ArrayList<BPMNProfile_Rendering> bpmnprofile_renderings    ) {
        this.implementation = implementation;
        this.bpmnprofile_renderings = bpmnprofile_renderings;
    }

    public String getImplementation() {
        return implementation;
    }

    public void setImplementation(String implementation) {
        this.implementation = implementation;
    }

    public List<BPMNProfile_Rendering> getBpmnprofile_renderings() {
        return bpmnprofile_renderings;
    }

    public void addBpmnprofile_rendering(Bpmnprofile_rendering bpmnprofile_rendering) {
        this.bpmnprofile_renderings.add(bpmnprofile_rendering);
    }
    public BPMNProfile_OpaqueAction getBpmnprofile_opaqueaction() {
        return bpmnprofile_opaqueaction;
    }

    public void setBpmnprofile_opaqueaction(BPMNProfile_OpaqueAction bpmnprofile_opaqueaction) {
        this.bpmnprofile_opaqueaction = bpmnprofile_opaqueaction;
    }

}