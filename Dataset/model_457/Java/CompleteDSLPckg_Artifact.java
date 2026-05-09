





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Artifact extends NamedElement, Classifier, DeployedArtifact {

    private String fileName;





    private List<CompleteDSLPckg_Artifact> completedslpckg_artifacts;


    public CompleteDSLPckg_Artifact(
        String fileName    ) {
        super(
        );
        this.fileName = fileName;
        this.completedslpckg_artifacts = new ArrayList<>();
    }

    public CompleteDSLPckg_Artifact(
        String fileName        ArrayList<CompleteDSLPckg_Artifact> completedslpckg_artifacts    ) {
        this.fileName = fileName;
        this.completedslpckg_artifacts = completedslpckg_artifacts;
    }

    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }

    public List<CompleteDSLPckg_Artifact> getCompletedslpckg_artifacts() {
        return completedslpckg_artifacts;
    }

    public void addCompletedslpckg_artifact(Completedslpckg_artifact completedslpckg_artifact) {
        this.completedslpckg_artifacts.add(completedslpckg_artifact);
    }

}