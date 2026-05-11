





import java.util.List;
import java.util.ArrayList;

public class bpmn2_LaneSet extends BaseElement, InteractionNode {






    private bpmn2_Lane bpmn2_lane;




    private List<bpmn2_Lane> bpmn2_lanes;




    private bpmn2_DocumentRoot bpmn2_documentroot;


    public bpmn2_LaneSet(
    ) {
        super(
        );
        this.bpmn2_lanes = new ArrayList<>();
    }

    public bpmn2_LaneSet(
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
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}