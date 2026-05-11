





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_FlowElementsContainer extends BaseElement {






    private List<bpmnprof_FlowElement> bpmnprof_flowelements;




    private bpmnprof_FlowElement bpmnprof_flowelement;


    public bpmnprof_FlowElementsContainer(
    ) {
        super(
        );
        this.bpmnprof_flowelements = new ArrayList<>();
    }

    public bpmnprof_FlowElementsContainer(
        ArrayList<bpmnprof_FlowElement> bpmnprof_flowelements    ) {
        this.bpmnprof_flowelements = bpmnprof_flowelements;
    }


    public List<bpmnprof_FlowElement> getBpmnprof_flowelements() {
        return bpmnprof_flowelements;
    }

    public void addBpmnprof_flowelement(Bpmnprof_flowelement bpmnprof_flowelement) {
        this.bpmnprof_flowelements.add(bpmnprof_flowelement);
    }
    public bpmnprof_FlowElement getBpmnprof_flowelement() {
        return bpmnprof_flowelement;
    }

    public void setBpmnprof_flowelement(bpmnprof_FlowElement bpmnprof_flowelement) {
        this.bpmnprof_flowelement = bpmnprof_flowelement;
    }

}