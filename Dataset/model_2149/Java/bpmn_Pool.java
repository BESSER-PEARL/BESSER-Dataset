





import java.util.List;
import java.util.ArrayList;

public class bpmn_Pool extends Graph, MessageVertex {






    private bpmn_Lane bpmn_lane;




    private List<bpmn_Lane> bpmn_lanes;


    public bpmn_Pool(
    ) {
        super(
        );
        this.bpmn_lanes = new ArrayList<>();
    }

    public bpmn_Pool(
        ArrayList<bpmn_Lane> bpmn_lanes    ) {
        this.bpmn_lanes = bpmn_lanes;
    }


    public bpmn_Lane getBpmn_lane() {
        return bpmn_lane;
    }

    public void setBpmn_lane(bpmn_Lane bpmn_lane) {
        this.bpmn_lane = bpmn_lane;
    }
    public List<bpmn_Lane> getBpmn_lanes() {
        return bpmn_lanes;
    }

    public void addBpmn_lane(Bpmn_lane bpmn_lane) {
        this.bpmn_lanes.add(bpmn_lane);
    }

}