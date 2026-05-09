





import java.util.List;
import java.util.ArrayList;

public class UML2_Artifact extends Classifier, DeployedArtifact {

    private String fileName;





    private List<UML2_Operation> uml2_operations;




    private List<UML2_Artifact> uml2_artifacts;




    private List<UML2_Manifestation> uml2_manifestations;


    public UML2_Artifact(
        String fileName    ) {
        super(
        );
        this.fileName = fileName;
        this.uml2_operations = new ArrayList<>();
        this.uml2_artifacts = new ArrayList<>();
        this.uml2_manifestations = new ArrayList<>();
    }

    public UML2_Artifact(
        String fileName        ArrayList<UML2_Operation> uml2_operations,        ArrayList<UML2_Artifact> uml2_artifacts,        ArrayList<UML2_Manifestation> uml2_manifestations    ) {
        this.fileName = fileName;
        this.uml2_operations = uml2_operations;
        this.uml2_artifacts = uml2_artifacts;
        this.uml2_manifestations = uml2_manifestations;
    }

    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }

    public List<UML2_Operation> getUml2_operations() {
        return uml2_operations;
    }

    public void addUml2_operation(Uml2_operation uml2_operation) {
        this.uml2_operations.add(uml2_operation);
    }
    public List<UML2_Artifact> getUml2_artifacts() {
        return uml2_artifacts;
    }

    public void addUml2_artifact(Uml2_artifact uml2_artifact) {
        this.uml2_artifacts.add(uml2_artifact);
    }
    public List<UML2_Manifestation> getUml2_manifestations() {
        return uml2_manifestations;
    }

    public void addUml2_manifestation(Uml2_manifestation uml2_manifestation) {
        this.uml2_manifestations.add(uml2_manifestation);
    }

}