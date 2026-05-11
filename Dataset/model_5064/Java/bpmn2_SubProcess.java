





import java.util.List;
import java.util.ArrayList;

public class bpmn2_SubProcess extends FlowElementsContainer, Activity {

    private boolean triggeredByEvent;





    private bpmn2_DocumentRoot bpmn2_documentroot;




    private List<bpmn2_Process> bpmn2_processs;




    private List<bpmn2_Artifact> bpmn2_artifacts;


    public bpmn2_SubProcess(
        boolean triggeredByEvent    ) {
        super(
        );
        this.triggeredByEvent = triggeredByEvent;
        this.bpmn2_processs = new ArrayList<>();
        this.bpmn2_artifacts = new ArrayList<>();
    }

    public bpmn2_SubProcess(
        boolean triggeredByEvent        ArrayList<bpmn2_Process> bpmn2_processs,        ArrayList<bpmn2_Artifact> bpmn2_artifacts    ) {
        this.triggeredByEvent = triggeredByEvent;
        this.bpmn2_processs = bpmn2_processs;
        this.bpmn2_artifacts = bpmn2_artifacts;
    }

    public boolean getTriggeredbyevent() {
        return triggeredByEvent;
    }

    public void setTriggeredbyevent(boolean triggeredByEvent) {
        this.triggeredByEvent = triggeredByEvent;
    }

    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }
    public List<bpmn2_Process> getBpmn2_processs() {
        return bpmn2_processs;
    }

    public void addBpmn2_process(Bpmn2_process bpmn2_process) {
        this.bpmn2_processs.add(bpmn2_process);
    }
    public List<bpmn2_Artifact> getBpmn2_artifacts() {
        return bpmn2_artifacts;
    }

    public void addBpmn2_artifact(Bpmn2_artifact bpmn2_artifact) {
        this.bpmn2_artifacts.add(bpmn2_artifact);
    }

}