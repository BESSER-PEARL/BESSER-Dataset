





import java.util.List;
import java.util.ArrayList;

public class bpmn2_FlowElementsContainer extends BaseElement {






    private List<bpmn2_FlowElement> bpmn2_flowelements;




    private List<bpmn2_LaneSet> bpmn2_lanesets;


    public bpmn2_FlowElementsContainer(
    ) {
        super(
        );
        this.bpmn2_flowelements = new ArrayList<>();
        this.bpmn2_lanesets = new ArrayList<>();
    }

    public bpmn2_FlowElementsContainer(
        ArrayList<bpmn2_FlowElement> bpmn2_flowelements,        ArrayList<bpmn2_LaneSet> bpmn2_lanesets    ) {
        this.bpmn2_flowelements = bpmn2_flowelements;
        this.bpmn2_lanesets = bpmn2_lanesets;
    }


    public List<bpmn2_FlowElement> getBpmn2_flowelements() {
        return bpmn2_flowelements;
    }

    public void addBpmn2_flowelement(Bpmn2_flowelement bpmn2_flowelement) {
        this.bpmn2_flowelements.add(bpmn2_flowelement);
    }
    public List<bpmn2_LaneSet> getBpmn2_lanesets() {
        return bpmn2_lanesets;
    }

    public void addBpmn2_laneset(Bpmn2_laneset bpmn2_laneset) {
        this.bpmn2_lanesets.add(bpmn2_laneset);
    }

}