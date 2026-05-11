





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_FlowElementsContainer extends BaseElement {






    private List<BPMN2Model_LaneSet> bpmn2model_lanesets;




    private List<BPMN2Model_FlowElement> bpmn2model_flowelements;


    public BPMN2Model_FlowElementsContainer(
    ) {
        super(
        );
        this.bpmn2model_lanesets = new ArrayList<>();
        this.bpmn2model_flowelements = new ArrayList<>();
    }

    public BPMN2Model_FlowElementsContainer(
        ArrayList<BPMN2Model_LaneSet> bpmn2model_lanesets,        ArrayList<BPMN2Model_FlowElement> bpmn2model_flowelements    ) {
        this.bpmn2model_lanesets = bpmn2model_lanesets;
        this.bpmn2model_flowelements = bpmn2model_flowelements;
    }


    public List<BPMN2Model_LaneSet> getBpmn2model_lanesets() {
        return bpmn2model_lanesets;
    }

    public void addBpmn2model_laneset(Bpmn2model_laneset bpmn2model_laneset) {
        this.bpmn2model_lanesets.add(bpmn2model_laneset);
    }
    public List<BPMN2Model_FlowElement> getBpmn2model_flowelements() {
        return bpmn2model_flowelements;
    }

    public void addBpmn2model_flowelement(Bpmn2model_flowelement bpmn2model_flowelement) {
        this.bpmn2model_flowelements.add(bpmn2model_flowelement);
    }

}