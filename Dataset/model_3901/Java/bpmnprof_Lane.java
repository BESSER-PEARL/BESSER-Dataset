





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_Lane extends BaseElement {






    private List<bpmnprof_FlowNode> bpmnprof_flownodes;




    private bpmnprof_BaseElement bpmnprof_baseelement;




    private bpmnprof_Element bpmnprof_element;


    public bpmnprof_Lane(
    ) {
        super(
        );
        this.bpmnprof_flownodes = new ArrayList<>();
    }

    public bpmnprof_Lane(
        ArrayList<bpmnprof_FlowNode> bpmnprof_flownodes    ) {
        this.bpmnprof_flownodes = bpmnprof_flownodes;
    }


    public List<bpmnprof_FlowNode> getBpmnprof_flownodes() {
        return bpmnprof_flownodes;
    }

    public void addBpmnprof_flownode(Bpmnprof_flownode bpmnprof_flownode) {
        this.bpmnprof_flownodes.add(bpmnprof_flownode);
    }
    public bpmnprof_BaseElement getBpmnprof_baseelement() {
        return bpmnprof_baseelement;
    }

    public void setBpmnprof_baseelement(bpmnprof_BaseElement bpmnprof_baseelement) {
        this.bpmnprof_baseelement = bpmnprof_baseelement;
    }
    public bpmnprof_Element getBpmnprof_element() {
        return bpmnprof_element;
    }

    public void setBpmnprof_element(bpmnprof_Element bpmnprof_element) {
        this.bpmnprof_element = bpmnprof_element;
    }

}