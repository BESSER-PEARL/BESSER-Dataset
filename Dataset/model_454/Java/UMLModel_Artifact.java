





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Artifact extends DeployedArtifact, Classifier {

    private String fileName;





    private List<UMLModel_Operation> umlmodel_operations;




    private UMLModel_Artifact umlmodel_artifact;


    public UMLModel_Artifact(
        String fileName    ) {
        super(
        );
        this.fileName = fileName;
        this.umlmodel_operations = new ArrayList<>();
    }

    public UMLModel_Artifact(
        String fileName        ArrayList<UMLModel_Operation> umlmodel_operations    ) {
        this.fileName = fileName;
        this.umlmodel_operations = umlmodel_operations;
    }

    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }

    public List<UMLModel_Operation> getUmlmodel_operations() {
        return umlmodel_operations;
    }

    public void addUmlmodel_operation(Umlmodel_operation umlmodel_operation) {
        this.umlmodel_operations.add(umlmodel_operation);
    }
    public UMLModel_Artifact getUmlmodel_artifact() {
        return umlmodel_artifact;
    }

    public void setUmlmodel_artifact(UMLModel_Artifact umlmodel_artifact) {
        this.umlmodel_artifact = umlmodel_artifact;
    }

}