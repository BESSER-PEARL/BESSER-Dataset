





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Artifact extends DeployedArtifact, Classifier {

    private String fileName;





    private List<uml3_0_0_Artifact> uml3_0_0_artifacts;




    private List<uml3_0_0_Operation> uml3_0_0_operations;


    public uml3_0_0_Artifact(
        String fileName    ) {
        super(
        );
        this.fileName = fileName;
        this.uml3_0_0_artifacts = new ArrayList<>();
        this.uml3_0_0_operations = new ArrayList<>();
    }

    public uml3_0_0_Artifact(
        String fileName        ArrayList<uml3_0_0_Artifact> uml3_0_0_artifacts,        ArrayList<uml3_0_0_Operation> uml3_0_0_operations    ) {
        this.fileName = fileName;
        this.uml3_0_0_artifacts = uml3_0_0_artifacts;
        this.uml3_0_0_operations = uml3_0_0_operations;
    }

    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }

    public List<uml3_0_0_Artifact> getUml3_0_0_artifacts() {
        return uml3_0_0_artifacts;
    }

    public void addUml3_0_0_artifact(Uml3_0_0_artifact uml3_0_0_artifact) {
        this.uml3_0_0_artifacts.add(uml3_0_0_artifact);
    }
    public List<uml3_0_0_Operation> getUml3_0_0_operations() {
        return uml3_0_0_operations;
    }

    public void addUml3_0_0_operation(Uml3_0_0_operation uml3_0_0_operation) {
        this.uml3_0_0_operations.add(uml3_0_0_operation);
    }

}