





import java.util.List;
import java.util.ArrayList;

public class UML2_Artifact extends DeployedArtifact, Classifier {

    private String fileName;





    private List<UML2_Operation> uml2_operations;




    private UML2_Artifact uml2_artifact;




    private List<UML2_Property> uml2_propertys;


    public UML2_Artifact(
        String fileName    ) {
        super(
        );
        this.fileName = fileName;
        this.uml2_operations = new ArrayList<>();
        this.uml2_propertys = new ArrayList<>();
    }

    public UML2_Artifact(
        String fileName        ArrayList<UML2_Operation> uml2_operations,        ArrayList<UML2_Property> uml2_propertys    ) {
        this.fileName = fileName;
        this.uml2_operations = uml2_operations;
        this.uml2_propertys = uml2_propertys;
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
    public UML2_Artifact getUml2_artifact() {
        return uml2_artifact;
    }

    public void setUml2_artifact(UML2_Artifact uml2_artifact) {
        this.uml2_artifact = uml2_artifact;
    }
    public List<UML2_Property> getUml2_propertys() {
        return uml2_propertys;
    }

    public void addUml2_property(Uml2_property uml2_property) {
        this.uml2_propertys.add(uml2_property);
    }

}