





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_UserTask extends Task {

    private String implementation;





    private List<BPMNProfile_Rendering> bpmnprofile_renderings;


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

}