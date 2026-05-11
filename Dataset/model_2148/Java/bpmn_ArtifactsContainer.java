





import java.util.List;
import java.util.ArrayList;

public class bpmn_ArtifactsContainer extends NamedBpmnObject {






    private bpmn_Artifact bpmn_artifact;




    private List<bpmn_Artifact> bpmn_artifacts;


    public bpmn_ArtifactsContainer(
    ) {
        super(
        );
        this.bpmn_artifacts = new ArrayList<>();
    }

    public bpmn_ArtifactsContainer(
        ArrayList<bpmn_Artifact> bpmn_artifacts    ) {
        this.bpmn_artifacts = bpmn_artifacts;
    }


    public bpmn_Artifact getBpmn_artifact() {
        return bpmn_artifact;
    }

    public void setBpmn_artifact(bpmn_Artifact bpmn_artifact) {
        this.bpmn_artifact = bpmn_artifact;
    }
    public List<bpmn_Artifact> getBpmn_artifacts() {
        return bpmn_artifacts;
    }

    public void addBpmn_artifact(Bpmn_artifact bpmn_artifact) {
        this.bpmn_artifacts.add(bpmn_artifact);
    }

}