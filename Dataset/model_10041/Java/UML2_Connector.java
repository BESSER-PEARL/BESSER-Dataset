





import java.util.List;
import java.util.ArrayList;

public class UML2_Connector extends Feature {

    private String kind;





    private List<UML2_ConnectorEnd> uml2_connectorends;




    private UML2_Association uml2_association;




    private UML2_StructuredClassifier uml2_structuredclassifier;




    private List<UML2_Behavior> uml2_behaviors;




    private UML2_Message uml2_message;




    private UML2_Connector uml2_connector;


    public UML2_Connector(
        String kind    ) {
        super(
        );
        this.kind = kind;
        this.uml2_connectorends = new ArrayList<>();
        this.uml2_behaviors = new ArrayList<>();
    }

    public UML2_Connector(
        String kind        ArrayList<UML2_ConnectorEnd> uml2_connectorends,        ArrayList<UML2_Behavior> uml2_behaviors    ) {
        this.kind = kind;
        this.uml2_connectorends = uml2_connectorends;
        this.uml2_behaviors = uml2_behaviors;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
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
    public UML2_StructuredClassifier getUml2_structuredclassifier() {
        return uml2_structuredclassifier;
    }

    public void setUml2_structuredclassifier(UML2_StructuredClassifier uml2_structuredclassifier) {
        this.uml2_structuredclassifier = uml2_structuredclassifier;
    }
    public List<UML2_Behavior> getUml2_behaviors() {
        return uml2_behaviors;
    }

    public void addUml2_behavior(Uml2_behavior uml2_behavior) {
        this.uml2_behaviors.add(uml2_behavior);
    }
    public UML2_Message getUml2_message() {
        return uml2_message;
    }

    public void setUml2_message(UML2_Message uml2_message) {
        this.uml2_message = uml2_message;
    }
    public UML2_Connector getUml2_connector() {
        return uml2_connector;
    }

    public void setUml2_connector(UML2_Connector uml2_connector) {
        this.uml2_connector = uml2_connector;
    }

}