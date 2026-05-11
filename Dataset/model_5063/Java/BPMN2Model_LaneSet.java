





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_LaneSet extends BaseElement {

    private String name;





    private List<BPMN2Model_Lane> bpmn2model_lanes;




    private BPMN2Model_Lane bpmn2model_lane;


    public BPMN2Model_LaneSet(
        String name    ) {
        super(
        );
        this.name = name;
        this.bpmn2model_lanes = new ArrayList<>();
    }

    public BPMN2Model_LaneSet(
        String name        ArrayList<BPMN2Model_Lane> bpmn2model_lanes    ) {
        this.name = name;
        this.bpmn2model_lanes = bpmn2model_lanes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<BPMN2Model_Lane> getBpmn2model_lanes() {
        return bpmn2model_lanes;
    }

    public void addBpmn2model_lane(Bpmn2model_lane bpmn2model_lane) {
        this.bpmn2model_lanes.add(bpmn2model_lane);
    }
    public BPMN2Model_Lane getBpmn2model_lane() {
        return bpmn2model_lane;
    }

    public void setBpmn2model_lane(BPMN2Model_Lane bpmn2model_lane) {
        this.bpmn2model_lane = bpmn2model_lane;
    }

}