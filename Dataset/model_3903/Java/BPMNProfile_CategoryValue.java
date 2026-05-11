





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_CategoryValue extends BaseElement {






    private BPMNProfile_Group bpmnprofile_group;




    private BPMNProfile_Category bpmnprofile_category;




    private List<BPMNProfile_FlowElement> bpmnprofile_flowelements;




    private BPMNProfile_FlowElement bpmnprofile_flowelement;


    public BPMNProfile_CategoryValue(
    ) {
        super(
        );
        this.bpmnprofile_flowelements = new ArrayList<>();
    }

    public BPMNProfile_CategoryValue(
        ArrayList<BPMNProfile_FlowElement> bpmnprofile_flowelements    ) {
        this.bpmnprofile_flowelements = bpmnprofile_flowelements;
    }


    public BPMNProfile_Group getBpmnprofile_group() {
        return bpmnprofile_group;
    }

    public void setBpmnprofile_group(BPMNProfile_Group bpmnprofile_group) {
        this.bpmnprofile_group = bpmnprofile_group;
    }
    public BPMNProfile_Category getBpmnprofile_category() {
        return bpmnprofile_category;
    }

    public void setBpmnprofile_category(BPMNProfile_Category bpmnprofile_category) {
        this.bpmnprofile_category = bpmnprofile_category;
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