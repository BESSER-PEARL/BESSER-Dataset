





import java.util.List;
import java.util.ArrayList;

public class bpmn_Activity extends Vertex, MessageVertex {

    private String activityType;
    private String looping;





    private bpmn_SubProcess bpmn_subprocess;




    private bpmn_SubProcess bpmn_subprocess;




    private List<bpmn_Lane> bpmn_lanes;




    private List<bpmn_Group> bpmn_groups;




    private bpmn_Group bpmn_group;




    private bpmn_Lane bpmn_lane;


    public bpmn_Activity(
        String activityType,        String looping    ) {
        super(
        );
        this.activityType = activityType;
        this.looping = looping;
        this.bpmn_lanes = new ArrayList<>();
        this.bpmn_groups = new ArrayList<>();
    }

    public bpmn_Activity(
        String activityType,        String looping        ArrayList<bpmn_Lane> bpmn_lanes,        ArrayList<bpmn_Group> bpmn_groups    ) {
        this.activityType = activityType;
        this.looping = looping;
        this.bpmn_lanes = bpmn_lanes;
        this.bpmn_groups = bpmn_groups;
    }

    public String getActivitytype() {
        return activityType;
    }

    public void setActivitytype(String activityType) {
        this.activityType = activityType;
    }
    public String getLooping() {
        return looping;
    }

    public void setLooping(String looping) {
        this.looping = looping;
    }

    public bpmn_SubProcess getBpmn_subprocess() {
        return bpmn_subprocess;
    }

    public void setBpmn_subprocess(bpmn_SubProcess bpmn_subprocess) {
        this.bpmn_subprocess = bpmn_subprocess;
    }
    public bpmn_SubProcess getBpmn_subprocess() {
        return bpmn_subprocess;
    }

    public void setBpmn_subprocess(bpmn_SubProcess bpmn_subprocess) {
        this.bpmn_subprocess = bpmn_subprocess;
    }
    public List<bpmn_Lane> getBpmn_lanes() {
        return bpmn_lanes;
    }

    public void addBpmn_lane(Bpmn_lane bpmn_lane) {
        this.bpmn_lanes.add(bpmn_lane);
    }
    public List<bpmn_Group> getBpmn_groups() {
        return bpmn_groups;
    }

    public void addBpmn_group(Bpmn_group bpmn_group) {
        this.bpmn_groups.add(bpmn_group);
    }
    public bpmn_Group getBpmn_group() {
        return bpmn_group;
    }

    public void setBpmn_group(bpmn_Group bpmn_group) {
        this.bpmn_group = bpmn_group;
    }
    public bpmn_Lane getBpmn_lane() {
        return bpmn_lane;
    }

    public void setBpmn_lane(bpmn_Lane bpmn_lane) {
        this.bpmn_lane = bpmn_lane;
    }

}