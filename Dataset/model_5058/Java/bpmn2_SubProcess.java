





import java.util.List;
import java.util.ArrayList;

public class bpmn2_SubProcess extends FlowElementsContainer, Activity {

    private boolean triggeredByEvent;





    private List<bpmn2_Artifact> bpmn2_artifacts;


    public bpmn2_SubProcess(
        boolean triggeredByEvent    ) {
        super(
        );
        this.triggeredByEvent = triggeredByEvent;
        this.bpmn2_artifacts = new ArrayList<>();
    }

    public bpmn2_SubProcess(
        boolean triggeredByEvent        ArrayList<bpmn2_Artifact> bpmn2_artifacts    ) {
        this.triggeredByEvent = triggeredByEvent;
        this.bpmn2_artifacts = bpmn2_artifacts;
    }

    public boolean getTriggeredbyevent() {
        return triggeredByEvent;
    }

    public void setTriggeredbyevent(boolean triggeredByEvent) {
        this.triggeredByEvent = triggeredByEvent;
    }

    public List<bpmn2_Artifact> getBpmn2_artifacts() {
        return bpmn2_artifacts;
    }

    public void addBpmn2_artifact(Bpmn2_artifact bpmn2_artifact) {
        this.bpmn2_artifacts.add(bpmn2_artifact);
    }

}