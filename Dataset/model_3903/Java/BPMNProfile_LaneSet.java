





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_LaneSet extends BaseElement {






    private BPMNProfile_Lane bpmnprofile_lane;




    private List<BPMNProfile_Lane> bpmnprofile_lanes;




    private List<BPMNProfile_Lane> bpmnprofile_lanes;




    private BPMNProfile_Lane bpmnprofile_lane;




    private BPMNProfile_SubProcess bpmnprofile_subprocess;


    public BPMNProfile_LaneSet(
    ) {
        super(
        );
        this.bpmnprofile_lanes = new ArrayList<>();
        this.bpmnprofile_lanes = new ArrayList<>();
    }

    public BPMNProfile_LaneSet(
        ArrayList<BPMNProfile_Lane> bpmnprofile_lanes,        ArrayList<BPMNProfile_Lane> bpmnprofile_lanes    ) {
        this.bpmnprofile_lanes = bpmnprofile_lanes;
        this.bpmnprofile_lanes = bpmnprofile_lanes;
    }


    public BPMNProfile_Lane getBpmnprofile_lane() {
        return bpmnprofile_lane;
    }

    public void setBpmnprofile_lane(BPMNProfile_Lane bpmnprofile_lane) {
        this.bpmnprofile_lane = bpmnprofile_lane;
    }
    public List<BPMNProfile_Lane> getBpmnprofile_lanes() {
        return bpmnprofile_lanes;
    }

    public void addBpmnprofile_lane(Bpmnprofile_lane bpmnprofile_lane) {
        this.bpmnprofile_lanes.add(bpmnprofile_lane);
    }
    public List<BPMNProfile_Lane> getBpmnprofile_lanes() {
        return bpmnprofile_lanes;
    }

    public void addBpmnprofile_lane(Bpmnprofile_lane bpmnprofile_lane) {
        this.bpmnprofile_lanes.add(bpmnprofile_lane);
    }
    public BPMNProfile_Lane getBpmnprofile_lane() {
        return bpmnprofile_lane;
    }

    public void setBpmnprofile_lane(BPMNProfile_Lane bpmnprofile_lane) {
        this.bpmnprofile_lane = bpmnprofile_lane;
    }
    public BPMNProfile_SubProcess getBpmnprofile_subprocess() {
        return bpmnprofile_subprocess;
    }

    public void setBpmnprofile_subprocess(BPMNProfile_SubProcess bpmnprofile_subprocess) {
        this.bpmnprofile_subprocess = bpmnprofile_subprocess;
    }

}