





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Connector extends Feature {

    private String kind;





    private List<UML2WithID_Behavior> uml2withid_behaviors;




    private List<UML2WithID_ConnectorEnd> uml2withid_connectorends;




    private UML2WithID_Association uml2withid_association;




    private UML2WithID_Message uml2withid_message;




    private UML2WithID_StructuredClassifier uml2withid_structuredclassifier;




    private UML2WithID_Connector uml2withid_connector;


    public UML2WithID_Connector(
        String kind    ) {
        super(
        );
        this.kind = kind;
        this.uml2withid_behaviors = new ArrayList<>();
        this.uml2withid_connectorends = new ArrayList<>();
    }

    public UML2WithID_Connector(
        String kind        ArrayList<UML2WithID_Behavior> uml2withid_behaviors,        ArrayList<UML2WithID_ConnectorEnd> uml2withid_connectorends    ) {
        this.kind = kind;
        this.uml2withid_behaviors = uml2withid_behaviors;
        this.uml2withid_connectorends = uml2withid_connectorends;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public List<UML2WithID_Behavior> getUml2withid_behaviors() {
        return uml2withid_behaviors;
    }

    public void addUml2withid_behavior(Uml2withid_behavior uml2withid_behavior) {
        this.uml2withid_behaviors.add(uml2withid_behavior);
    }
    public List<UML2WithID_ConnectorEnd> getUml2withid_connectorends() {
        return uml2withid_connectorends;
    }

    public void addUml2withid_connectorend(Uml2withid_connectorend uml2withid_connectorend) {
        this.uml2withid_connectorends.add(uml2withid_connectorend);
    }
    public UML2WithID_Association getUml2withid_association() {
        return uml2withid_association;
    }

    public void setUml2withid_association(UML2WithID_Association uml2withid_association) {
        this.uml2withid_association = uml2withid_association;
    }
    public UML2WithID_Message getUml2withid_message() {
        return uml2withid_message;
    }

    public void setUml2withid_message(UML2WithID_Message uml2withid_message) {
        this.uml2withid_message = uml2withid_message;
    }
    public UML2WithID_StructuredClassifier getUml2withid_structuredclassifier() {
        return uml2withid_structuredclassifier;
    }

    public void setUml2withid_structuredclassifier(UML2WithID_StructuredClassifier uml2withid_structuredclassifier) {
        this.uml2withid_structuredclassifier = uml2withid_structuredclassifier;
    }
    public UML2WithID_Connector getUml2withid_connector() {
        return uml2withid_connector;
    }

    public void setUml2withid_connector(UML2WithID_Connector uml2withid_connector) {
        this.uml2withid_connector = uml2withid_connector;
    }

}