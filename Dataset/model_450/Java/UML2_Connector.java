





import java.util.List;
import java.util.ArrayList;

public class UML2_Connector extends Feature {

    private String kind;





    private UML2_StructuredClassifier uml2_structuredclassifier;




    private List<UML2_Connector> uml2_connectors;




    private List<UML2_ConnectorEnd> uml2_connectorends;




    private UML2_Association uml2_association;


    public UML2_Connector(
        String kind    ) {
        super(
        );
        this.kind = kind;
        this.uml2_connectors = new ArrayList<>();
        this.uml2_connectorends = new ArrayList<>();
    }

    public UML2_Connector(
        String kind        ArrayList<UML2_Connector> uml2_connectors,        ArrayList<UML2_ConnectorEnd> uml2_connectorends    ) {
        this.kind = kind;
        this.uml2_connectors = uml2_connectors;
        this.uml2_connectorends = uml2_connectorends;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public UML2_StructuredClassifier getUml2_structuredclassifier() {
        return uml2_structuredclassifier;
    }

    public void setUml2_structuredclassifier(UML2_StructuredClassifier uml2_structuredclassifier) {
        this.uml2_structuredclassifier = uml2_structuredclassifier;
    }
    public List<UML2_Connector> getUml2_connectors() {
        return uml2_connectors;
    }

    public void addUml2_connector(Uml2_connector uml2_connector) {
        this.uml2_connectors.add(uml2_connector);
    }
    public List<UML2_ConnectorEnd> getUml2_connectorends() {
        return uml2_connectorends;
    }

    public void addUml2_connectorend(Uml2_connectorend uml2_connectorend) {
        this.uml2_connectorends.add(uml2_connectorend);
    }
    public UML2_Association getUml2_association() {
        return uml2_association;
    }

    public void setUml2_association(UML2_Association uml2_association) {
        this.uml2_association = uml2_association;
    }

}