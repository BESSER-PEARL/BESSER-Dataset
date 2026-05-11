





import java.util.List;
import java.util.ArrayList;

public class bpmn2_FlowNode extends FlowElement {






    private bpmn2_Lane bpmn2_lane;




    private List<bpmn2_Lane> bpmn2_lanes;


    public bpmn2_FlowNode(
    ) {
        super(
        );
        this.bpmn2_lanes = new ArrayList<>();
    }

    public bpmn2_FlowNode(
        ArrayList<bpmn2_Lane> bpmn2_lanes    ) {
        this.bpmn2_lanes = bpmn2_lanes;
    }


    public bpmn2_Lane getBpmn2_lane() {
        return bpmn2_lane;
    }

    public void setBpmn2_lane(bpmn2_Lane bpmn2_lane) {
        this.bpmn2_lane = bpmn2_lane;
    }
    public List<bpmn2_Lane> getBpmn2_lanes() {
        return bpmn2_lanes;
    }

    public void addBpmn2_lane(Bpmn2_lane bpmn2_lane) {
        this.bpmn2_lanes.add(bpmn2_lane);
    }

}