





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_FlowElementsContainer extends BaseElement {






    private List<BPMNProfile_FlowElement> bpmnprofile_flowelements;




    private BPMNProfile_FlowElement bpmnprofile_flowelement;


    public BPMNProfile_FlowElementsContainer(
    ) {
        super(
        );
        this.bpmnprofile_flowelements = new ArrayList<>();
    }

    public BPMNProfile_FlowElementsContainer(
        ArrayList<BPMNProfile_FlowElement> bpmnprofile_flowelements    ) {
        this.bpmnprofile_flowelements = bpmnprofile_flowelements;
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

}