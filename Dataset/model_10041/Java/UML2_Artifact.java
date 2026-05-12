





import java.util.List;
import java.util.ArrayList;

public class UML2_Artifact extends DeployedArtifact, Classifier {

    private String fileName;





    private List<UML2_Property> uml2_propertys;




    private List<UML2_Artifact> uml2_artifacts;




    private List<UML2_Operation> uml2_operations;


    public UML2_Artifact(
        String fileName    ) {
        super(
        );
        this.fileName = fileName;
        this.uml2_propertys = new ArrayList<>();
        this.uml2_artifacts = new ArrayList<>();
        this.uml2_operations = new ArrayList<>();
    }

    public UML2_Artifact(
        String fileName        ArrayList<UML2_Property> uml2_propertys,        ArrayList<UML2_Artifact> uml2_artifacts,        ArrayList<UML2_Operation> uml2_operations    ) {
        this.fileName = fileName;
        this.uml2_propertys = uml2_propertys;
        this.uml2_artifacts = uml2_artifacts;
        this.uml2_operations = uml2_operations;
    }

    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }

    public List<UML2_Property> getUml2_propertys() {
        return uml2_propertys;
    }

    public void addUml2_property(Uml2_property uml2_property) {
        this.uml2_propertys.add(uml2_property);
    }
    public List<UML2_Artifact> getUml2_artifacts() {
        return uml2_artifacts;
    }

    public void addUml2_artifact(Uml2_artifact uml2_artifact) {
        this.uml2_artifacts.add(uml2_artifact);
    }
    public List<UML2_Operation> getUml2_operations() {
        return uml2_operations;
    }

    public void addUml2_operation(Uml2_operation uml2_operation) {
        this.uml2_operations.add(uml2_operation);
    }

}