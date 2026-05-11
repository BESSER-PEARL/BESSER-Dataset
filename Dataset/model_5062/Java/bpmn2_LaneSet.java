





import java.util.List;
import java.util.ArrayList;

public class bpmn2_LaneSet extends BaseElement {

    private String name;





    private bpmn2_Lane bpmn2_lane;




    private List<bpmn2_Lane> bpmn2_lanes;




    private bpmn2_FlowElementsContainer bpmn2_flowelementscontainer;


    public bpmn2_LaneSet(
        String name    ) {
        super(
        );
        this.name = name;
        this.bpmn2_lanes = new ArrayList<>();
    }

    public bpmn2_LaneSet(
        String name        ArrayList<bpmn2_Lane> bpmn2_lanes    ) {
        this.name = name;
        this.bpmn2_lanes = bpmn2_lanes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public bpmn2_FlowElementsContainer getBpmn2_flowelementscontainer() {
        return bpmn2_flowelementscontainer;
    }

    public void setBpmn2_flowelementscontainer(bpmn2_FlowElementsContainer bpmn2_flowelementscontainer) {
        this.bpmn2_flowelementscontainer = bpmn2_flowelementscontainer;
    }

}