





import java.util.List;
import java.util.ArrayList;

public class UMLModel_StructuredClassifier extends Classifier {

    private String part;
    private String role;





    private List<UMLModel_Connector> umlmodel_connectors;


    public UMLModel_StructuredClassifier(
        String part,        String role    ) {
        super(
        );
        this.part = part;
        this.role = role;
        this.umlmodel_connectors = new ArrayList<>();
    }

    public UMLModel_StructuredClassifier(
        String part,        String role        ArrayList<UMLModel_Connector> umlmodel_connectors    ) {
        this.part = part;
        this.role = role;
        this.umlmodel_connectors = umlmodel_connectors;
    }

    public String getPart() {
        return part;
    }

    public void setPart(String part) {
        this.part = part;
    }
    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }

    public List<UMLModel_Connector> getUmlmodel_connectors() {
        return umlmodel_connectors;
    }

    public void addUmlmodel_connector(Umlmodel_connector umlmodel_connector) {
        this.umlmodel_connectors.add(umlmodel_connector);
    }

}