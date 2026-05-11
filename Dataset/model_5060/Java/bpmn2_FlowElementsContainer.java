





import java.util.List;
import java.util.ArrayList;

public class bpmn2_FlowElementsContainer extends BaseElement {






    private List<bpmn2_FlowElement> bpmn2_flowelements;


    public bpmn2_FlowElementsContainer(
    ) {
        super(
        );
        this.bpmn2_flowelements = new ArrayList<>();
    }

    public bpmn2_FlowElementsContainer(
        ArrayList<bpmn2_FlowElement> bpmn2_flowelements    ) {
        this.bpmn2_flowelements = bpmn2_flowelements;
    }


    public List<bpmn2_FlowElement> getBpmn2_flowelements() {
        return bpmn2_flowelements;
    }

    public void addBpmn2_flowelement(Bpmn2_flowelement bpmn2_flowelement) {
        this.bpmn2_flowelements.add(bpmn2_flowelement);
    }

}