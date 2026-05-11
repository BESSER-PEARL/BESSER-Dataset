





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_LaneSet extends BaseElement {






    private bpmnprof_Lane bpmnprof_lane;




    private bpmnprof_FlowElementsContainer bpmnprof_flowelementscontainer;




    private bpmnprof_Lane bpmnprof_lane;




    private bpmnprof_FlowElementsContainer bpmnprof_flowelementscontainer;




    private List<bpmnprof_Lane> bpmnprof_lanes;




    private List<bpmnprof_Lane> bpmnprof_lanes;


    public bpmnprof_LaneSet(
    ) {
        super(
        );
        this.bpmnprof_lanes = new ArrayList<>();
        this.bpmnprof_lanes = new ArrayList<>();
    }

    public bpmnprof_LaneSet(
        ArrayList<bpmnprof_Lane> bpmnprof_lanes,        ArrayList<bpmnprof_Lane> bpmnprof_lanes    ) {
        this.bpmnprof_lanes = bpmnprof_lanes;
        this.bpmnprof_lanes = bpmnprof_lanes;
    }


    public bpmnprof_Lane getBpmnprof_lane() {
        return bpmnprof_lane;
    }

    public void setBpmnprof_lane(bpmnprof_Lane bpmnprof_lane) {
        this.bpmnprof_lane = bpmnprof_lane;
    }
    public bpmnprof_FlowElementsContainer getBpmnprof_flowelementscontainer() {
        return bpmnprof_flowelementscontainer;
    }

    public void setBpmnprof_flowelementscontainer(bpmnprof_FlowElementsContainer bpmnprof_flowelementscontainer) {
        this.bpmnprof_flowelementscontainer = bpmnprof_flowelementscontainer;
    }
    public bpmnprof_Lane getBpmnprof_lane() {
        return bpmnprof_lane;
    }

    public void setBpmnprof_lane(bpmnprof_Lane bpmnprof_lane) {
        this.bpmnprof_lane = bpmnprof_lane;
    }
    public bpmnprof_FlowElementsContainer getBpmnprof_flowelementscontainer() {
        return bpmnprof_flowelementscontainer;
    }

    public void setBpmnprof_flowelementscontainer(bpmnprof_FlowElementsContainer bpmnprof_flowelementscontainer) {
        this.bpmnprof_flowelementscontainer = bpmnprof_flowelementscontainer;
    }
    public List<bpmnprof_Lane> getBpmnprof_lanes() {
        return bpmnprof_lanes;
    }

    public void addBpmnprof_lane(Bpmnprof_lane bpmnprof_lane) {
        this.bpmnprof_lanes.add(bpmnprof_lane);
    }
    public List<bpmnprof_Lane> getBpmnprof_lanes() {
        return bpmnprof_lanes;
    }

    public void addBpmnprof_lane(Bpmnprof_lane bpmnprof_lane) {
        this.bpmnprof_lanes.add(bpmnprof_lane);
    }

}