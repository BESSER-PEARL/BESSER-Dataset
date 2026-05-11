





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_SubProcess extends BPMNActivity, FlowElementsContainer {

    private String triggeredByEvent;





    private bpmnprof_StructuredActivityNode bpmnprof_structuredactivitynode;




    private List<bpmnprof_LaneSet> bpmnprof_lanesets;


    public bpmnprof_SubProcess(
        String triggeredByEvent    ) {
        super(
        );
        this.triggeredByEvent = triggeredByEvent;
        this.bpmnprof_lanesets = new ArrayList<>();
    }

    public bpmnprof_SubProcess(
        String triggeredByEvent        ArrayList<bpmnprof_LaneSet> bpmnprof_lanesets    ) {
        this.triggeredByEvent = triggeredByEvent;
        this.bpmnprof_lanesets = bpmnprof_lanesets;
    }

    public String getTriggeredbyevent() {
        return triggeredByEvent;
    }

    public void setTriggeredbyevent(String triggeredByEvent) {
        this.triggeredByEvent = triggeredByEvent;
    }

    public bpmnprof_StructuredActivityNode getBpmnprof_structuredactivitynode() {
        return bpmnprof_structuredactivitynode;
    }

    public void setBpmnprof_structuredactivitynode(bpmnprof_StructuredActivityNode bpmnprof_structuredactivitynode) {
        this.bpmnprof_structuredactivitynode = bpmnprof_structuredactivitynode;
    }
    public List<bpmnprof_LaneSet> getBpmnprof_lanesets() {
        return bpmnprof_lanesets;
    }

    public void addBpmnprof_laneset(Bpmnprof_laneset bpmnprof_laneset) {
        this.bpmnprof_lanesets.add(bpmnprof_laneset);
    }

}