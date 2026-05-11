





import java.util.List;
import java.util.ArrayList;

public class bpmn2_SubChoreography extends ChoreographyActivity, FlowElementsContainer {






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


    public List<bpmn2_Artifact> getBpmn2_artifacts() {
        return bpmn2_artifacts;
    }

    public void addBpmn2_artifact(Bpmn2_artifact bpmn2_artifact) {
        this.bpmn2_artifacts.add(bpmn2_artifact);
    }

}