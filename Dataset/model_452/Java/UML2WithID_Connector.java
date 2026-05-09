





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Connector extends Feature {

    private String kind;





    private List<UML2WithID_Connector> uml2withid_connectors;




    private UML2WithID_Association uml2withid_association;




    private UML2WithID_StructuredClassifier uml2withid_structuredclassifier;


    public UML2WithID_Connector(
        String kind    ) {
        super(
        );
        this.kind = kind;
        this.uml2withid_connectors = new ArrayList<>();
    }

    public UML2WithID_Connector(
        String kind        ArrayList<UML2WithID_Connector> uml2withid_connectors    ) {
        this.kind = kind;
        this.uml2withid_connectors = uml2withid_connectors;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public List<UML2WithID_Connector> getUml2withid_connectors() {
        return uml2withid_connectors;
    }

    public void addUml2withid_connector(Uml2withid_connector uml2withid_connector) {
        this.uml2withid_connectors.add(uml2withid_connector);
    }
    public UML2WithID_Association getUml2withid_association() {
        return uml2withid_association;
    }

    public void setUml2withid_association(UML2WithID_Association uml2withid_association) {
        this.uml2withid_association = uml2withid_association;
    }
    public UML2WithID_StructuredClassifier getUml2withid_structuredclassifier() {
        return uml2withid_structuredclassifier;
    }

    public void setUml2withid_structuredclassifier(UML2WithID_StructuredClassifier uml2withid_structuredclassifier) {
        this.uml2withid_structuredclassifier = uml2withid_structuredclassifier;
    }

}