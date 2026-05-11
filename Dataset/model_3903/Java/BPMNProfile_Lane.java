





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_Lane extends BaseElement {






    private List<BPMNProfile_FlowNode> bpmnprofile_flownodes;


    public BPMNProfile_Lane(
    ) {
        super(
        );
        this.bpmnprofile_flownodes = new ArrayList<>();
    }

    public BPMNProfile_Lane(
        ArrayList<BPMNProfile_FlowNode> bpmnprofile_flownodes    ) {
        this.bpmnprofile_flownodes = bpmnprofile_flownodes;
    }


    public List<BPMNProfile_FlowNode> getBpmnprofile_flownodes() {
        return bpmnprofile_flownodes;
    }

    public void addBpmnprofile_flownode(Bpmnprofile_flownode bpmnprofile_flownode) {
        this.bpmnprofile_flownodes.add(bpmnprofile_flownode);
    }

}