





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_FlowElementsContainer extends BaseElement {






    private List<BPMNProfile_LaneSet> bpmnprofile_lanesets;




    private List<BPMNProfile_FlowElement> bpmnprofile_flowelements;




    private BPMNProfile_FlowElement bpmnprofile_flowelement;




    private BPMNProfile_LaneSet bpmnprofile_laneset;


    public BPMNProfile_FlowElementsContainer(
    ) {
        super(
        );
        this.bpmnprofile_lanesets = new ArrayList<>();
        this.bpmnprofile_flowelements = new ArrayList<>();
    }

    public BPMNProfile_FlowElementsContainer(
        ArrayList<BPMNProfile_LaneSet> bpmnprofile_lanesets,        ArrayList<BPMNProfile_FlowElement> bpmnprofile_flowelements    ) {
        this.bpmnprofile_lanesets = bpmnprofile_lanesets;
        this.bpmnprofile_flowelements = bpmnprofile_flowelements;
    }


    public List<BPMNProfile_LaneSet> getBpmnprofile_lanesets() {
        return bpmnprofile_lanesets;
    }

    public void addBpmnprofile_laneset(Bpmnprofile_laneset bpmnprofile_laneset) {
        this.bpmnprofile_lanesets.add(bpmnprofile_laneset);
    }
    public List<BPMNProfile_FlowElement> getBpmnprofile_flowelements() {
        return bpmnprofile_flowelements;
    }

    public void addBpmnprofile_flowelement(Bpmnprofile_flowelement bpmnprofile_flowelement) {
        this.bpmnprofile_flowelements.add(bpmnprofile_flowelement);
    }
    public BPMNProfile_FlowElement getBpmnprofile_flowelement() {
        return bpmnprofile_flowelement;
    }

    public void setBpmnprofile_flowelement(BPMNProfile_FlowElement bpmnprofile_flowelement) {
        this.bpmnprofile_flowelement = bpmnprofile_flowelement;
    }
    public BPMNProfile_LaneSet getBpmnprofile_laneset() {
        return bpmnprofile_laneset;
    }

    public void setBpmnprofile_laneset(BPMNProfile_LaneSet bpmnprofile_laneset) {
        this.bpmnprofile_laneset = bpmnprofile_laneset;
    }

}