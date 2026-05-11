





import java.util.List;
import java.util.ArrayList;

public class bpmn2_SubChoreography extends FlowElementsContainer, ChoreographyActivity {






    private bpmn2_DocumentRoot bpmn2_documentroot;




    private List<bpmn2_Artifact> bpmn2_artifacts;


    public bpmn2_SubChoreography(
    ) {
        super(
        );
        this.bpmn2_artifacts = new ArrayList<>();
    }

    public bpmn2_SubChoreography(
        ArrayList<bpmn2_Artifact> bpmn2_artifacts    ) {
        this.bpmn2_artifacts = bpmn2_artifacts;
    }


    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }
    public List<bpmn2_Artifact> getBpmn2_artifacts() {
        return bpmn2_artifacts;
    }

    public void addBpmn2_artifact(Bpmn2_artifact bpmn2_artifact) {
        this.bpmn2_artifacts.add(bpmn2_artifact);
    }

}