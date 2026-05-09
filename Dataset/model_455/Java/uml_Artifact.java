





import java.util.List;
import java.util.ArrayList;

public class uml_Artifact extends Classifier, DeployedArtifact {

    private String fileName;





    private List<uml_Operation> uml_operations;




    private uml_Artifact uml_artifact;


    public uml_Artifact(
        String fileName    ) {
        super(
        );
        this.fileName = fileName;
        this.uml_operations = new ArrayList<>();
    }

    public uml_Artifact(
        String fileName        ArrayList<uml_Operation> uml_operations    ) {
        this.fileName = fileName;
        this.uml_operations = uml_operations;
    }

    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }

    public List<uml_Operation> getUml_operations() {
        return uml_operations;
    }

    public void addUml_operation(Uml_operation uml_operation) {
        this.uml_operations.add(uml_operation);
    }
    public uml_Artifact getUml_artifact() {
        return uml_artifact;
    }

    public void setUml_artifact(uml_Artifact uml_artifact) {
        this.uml_artifact = uml_artifact;
    }

}