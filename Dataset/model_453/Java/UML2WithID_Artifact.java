





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Artifact extends DeployedArtifact, Classifier {

    private String fileName;





    private UML2WithID_Artifact uml2withid_artifact;




    private List<UML2WithID_Operation> uml2withid_operations;




    private List<UML2WithID_Property> uml2withid_propertys;


    public UML2WithID_Artifact(
        String fileName    ) {
        super(
        );
        this.fileName = fileName;
        this.uml2withid_operations = new ArrayList<>();
        this.uml2withid_propertys = new ArrayList<>();
    }

    public UML2WithID_Artifact(
        String fileName        ArrayList<UML2WithID_Operation> uml2withid_operations,        ArrayList<UML2WithID_Property> uml2withid_propertys    ) {
        this.fileName = fileName;
        this.uml2withid_operations = uml2withid_operations;
        this.uml2withid_propertys = uml2withid_propertys;
    }

    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }

    public UML2WithID_Artifact getUml2withid_artifact() {
        return uml2withid_artifact;
    }

    public void setUml2withid_artifact(UML2WithID_Artifact uml2withid_artifact) {
        this.uml2withid_artifact = uml2withid_artifact;
    }
    public List<UML2WithID_Operation> getUml2withid_operations() {
        return uml2withid_operations;
    }

    public void addUml2withid_operation(Uml2withid_operation uml2withid_operation) {
        this.uml2withid_operations.add(uml2withid_operation);
    }
    public List<UML2WithID_Property> getUml2withid_propertys() {
        return uml2withid_propertys;
    }

    public void addUml2withid_property(Uml2withid_property uml2withid_property) {
        this.uml2withid_propertys.add(uml2withid_property);
    }

}